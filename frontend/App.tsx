import {
  Group,
  Text,
  useMantineTheme,
  Center,
  Flex,
  MantineProvider,
  ColorSchemeProvider,
  ColorScheme
} from '@mantine/core';
import { IconUpload, IconX } from '@tabler/icons-react';
import { Dropzone, DropzoneProps } from '@mantine/dropzone';
import { useState } from 'react';
import { useColorScheme } from '@mantine/hooks';

export default function App(props: Partial<DropzoneProps>) {
  const theme = useMantineTheme();
  const preferredColorScheme = useColorScheme();
  const [colorScheme, setColorScheme] =
    useState<ColorScheme>(preferredColorScheme);
  const toggleColorScheme = (value?: ColorScheme) =>
    setColorScheme(value || (colorScheme === 'dark' ? 'light' : 'dark'));
  const [loading, setLoading] = useState(false);
  const maxFileSize = import.meta.env.VITE_MAX_FILE_SIZE || 5 * 1024 * 1024;
  const handleDrop = async (files: File[]) => {
    setLoading(true);

    const formData = new FormData();

    for (const file of files) {
      formData.append('files', file);
    }

    try {
      const response = await fetch(
        import.meta.env.VITE_API_URL || 'http://localhost:8000',
        {
          method: 'POST',
          body: formData
        }
      );

      const blob = await response.blob();

      const now = new Date();
      const datetimeStamp = now.toISOString().replace(/[:.]/g, '-');

      const filename = `archive-${datetimeStamp}.zip`;

      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');

      link.href = url;
      link.download = filename;

      document.body.appendChild(link);
      link.click();

      document.body.removeChild(link);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ColorSchemeProvider
      colorScheme={colorScheme}
      toggleColorScheme={toggleColorScheme}>
      <MantineProvider
        withGlobalStyles
        withNormalizeCSS
        theme={{ colorScheme }}>
        <Flex
          align={'center'}
          justify={'center'}
          style={{ height: '100vh' }}
          mx={30}>
          <Center mx="auto">
            <Dropzone
              onDrop={files => handleDrop(files)}
              onReject={files => console.log('rejected files', files)}
              maxSize={maxFileSize}
              loading={loading}
              {...props}>
              <Group
                position="center"
                spacing="xl"
                py={60}
                px={20}
                style={{
                  pointerEvents: 'none'
                }}>
                <Dropzone.Accept>
                  <IconUpload
                    size="3.2rem"
                    stroke={1.5}
                    color={
                      theme.colors[theme.primaryColor][
                        theme.colorScheme === 'dark' ? 4 : 6
                      ]
                    }
                  />
                </Dropzone.Accept>
                <Dropzone.Reject>
                  <IconX
                    size="3.2rem"
                    stroke={1.5}
                    color={
                      theme.colors.red[theme.colorScheme === 'dark' ? 4 : 6]
                    }
                  />
                </Dropzone.Reject>
                <Dropzone.Idle>
                  <IconUpload size="3.2rem" stroke={1.5} />
                </Dropzone.Idle>
                <div>
                  <Text size="lg" inline>
                    Drag files here or tap to select files
                  </Text>
                  <Text size="sm" color="dimmed" inline mt={7}>
                    Attach as many files as you like.
                  </Text>
                  <Text size="sm" color="dimmed" inline mt={7}>
                    Filesize should not exceed{' '}
                    {Math.round(maxFileSize / 1024 / 1024)} MB.
                  </Text>
                </div>
              </Group>
            </Dropzone>
          </Center>
        </Flex>
      </MantineProvider>
    </ColorSchemeProvider>
  );
}
