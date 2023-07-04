import { Group, Text, useMantineTheme } from '@mantine/core';
import { IconUpload, IconX } from '@tabler/icons-react';
import { Dropzone } from '@mantine/dropzone';

interface DropzoneContentProps {
  loading: boolean;
  maxFileSize: number;
}

const DropzoneContent: React.FC<DropzoneContentProps> = ({ maxFileSize }) => {
  const theme = useMantineTheme();

  return (
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
          color={theme.colors.red[theme.colorScheme === 'dark' ? 4 : 6]}
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
          Filesize should not exceed {Math.round(maxFileSize / 1024 / 1024)} MB.
        </Text>
      </div>
    </Group>
  );
};

export default DropzoneContent;
