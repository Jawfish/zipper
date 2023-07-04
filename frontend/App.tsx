import { useState } from 'react';
import { useColorScheme } from '@mantine/hooks';
import {
  MantineProvider,
  ColorSchemeProvider,
  ColorScheme
} from '@mantine/core';

import Header from './Header';
import FileUploader from './FileUploader';
import { handleDrop, handleReject } from './fileHandling';

const App: React.FC = () => {
  const preferredColorScheme = useColorScheme();
  const [colorScheme, setColorScheme] =
    useState<ColorScheme>(preferredColorScheme);
  const [loading, setLoading] = useState(false);
  const maxFileSize = import.meta.env.VITE_MAX_FILE_SIZE || 5 * 1024 * 1024;

  const toggleColorScheme = (value?: ColorScheme) =>
    setColorScheme(value || (colorScheme === 'dark' ? 'light' : 'dark'));

  return (
    <ColorSchemeProvider
      colorScheme={colorScheme}
      toggleColorScheme={toggleColorScheme}>
      <MantineProvider
        withGlobalStyles
        withNormalizeCSS
        theme={{ colorScheme }}>
        <Header />
        <FileUploader
          handleDrop={handleDrop(setLoading)}
          handleReject={handleReject(maxFileSize)}
          maxFileSize={maxFileSize}
          loading={loading}
        />
      </MantineProvider>
    </ColorSchemeProvider>
  );
};

export default App;
