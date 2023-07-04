import { Center, Flex } from '@mantine/core';
import { Dropzone, DropzoneProps, FileRejection } from '@mantine/dropzone';

import DropZoneContent from './DropZoneContent';

import 'react-toastify/dist/ReactToastify.css';

interface FileUploaderProps extends Partial<DropzoneProps> {
  handleDrop: (files: File[]) => void;
  handleReject: (files: FileRejection[]) => void;
  maxFileSize: number;
  loading: boolean;
}

const FileUploader: React.FC<FileUploaderProps> = ({
  handleDrop,
  handleReject,
  maxFileSize,
  loading,
  ...props
}) => {
  return (
    <Flex align={'center'} justify={'center'} mx={30}>
      <Center mx="auto">
        <Dropzone
          onDrop={files => handleDrop(files)}
          onReject={files => {
            handleReject(files);
          }}
          maxSize={maxFileSize}
          loading={loading}
          {...props}>
          <DropZoneContent loading={loading} maxFileSize={maxFileSize} />
        </Dropzone>
      </Center>
    </Flex>
  );
};

export default FileUploader;
