import { FileRejection } from '@mantine/dropzone';
import { toast } from 'react-toastify';

export const handleDrop =
  (setLoading: React.Dispatch<React.SetStateAction<boolean>>) =>
  async (files: File[]) => {
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

      switch (response.status) {
        case 413:
          throw new Error('The server says the file size is too large.');
        case 400:
          throw new Error("The server couldn't find any files to process.");
        case 404:
          throw new Error('The server could not be reached.');
        case 200:
          break;
        default:
          throw new Error('An unexpected server-side error occurred.');
      }

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
      if (error instanceof Error) {
        toast.error(error.message);
      } else {
        toast.error('An unexpected error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

export const handleReject =
  (maxFileSize: number) => (rejections: FileRejection[]) => {
    rejections.forEach(rejection => {
      rejection.errors.forEach(error => {
        if (error.code === 'file-too-large') {
          toast.error(
            `File size should not exceed ${Math.round(
              maxFileSize / 1024 / 1024
            )} MB`
          );
        }
      });
    });
  };
