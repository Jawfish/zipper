import { Flex } from '@mantine/core';

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="p-4 text-center text-zinc-500">
      <Flex justify="center" gap={5}>
        <span>&copy;</span>
        <span>{year}</span>
        <a className="underline" href="https://jawfish.dev">
          James Fitzgerald
        </a>
      </Flex>
    </footer>
  );
}
