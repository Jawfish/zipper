import { Group, Text, useMantineTheme } from '@mantine/core';
import { useMediaQuery } from '@mantine/hooks';
import { IconUpload, IconX } from '@tabler/icons-react';
import { Dropzone } from '@mantine/dropzone';

interface DropzoneContentProps {
  loading: boolean;
  maxFileSize: number;
}

const DropzoneContent: React.FC<DropzoneContentProps> = ({ maxFileSize }) => {
  const theme = useMantineTheme();
  const isDesktop = useMediaQuery('(min-width: 960px)');

  const paddingY = isDesktop ? 100 : 60;
  const paddingX = isDesktop ? 100 : 20;

  return (
    <Group
      position="center"
      spacing="xl"
      py={paddingY}
      px={paddingX}
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
          color={theme.colors.red[theme.colorScheme === 'dark' ? 4 : 6]}
        />
      </Dropzone.Reject>
      <Dropzone.Idle>
        <IconUpload size="3.2rem" stroke={1.5} />
      </Dropzone.Idle>
      <div>
        <Text size="lg" inline>
          Select files to be zipped
        </Text>
        <Text size="sm" color="dimmed" inline mt={7}>
          Attach as many files as you like.
        </Text>
        <Text size="sm" color="dimmed" inline mt={7}>
          Filesize should not exceed {Math.round(maxFileSize / 1024 / 1024)} MB.
        </Text>
      </div>
    </Group>
  );
};

export default DropzoneContent;
