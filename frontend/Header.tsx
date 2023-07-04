import { Flex } from '@mantine/core';
import { IconFileZip } from '@tabler/icons-react';

export default function Header() {
  return (
    <header className="bg-blue-400/75 p-4 text-center text-white">
      <h1 className="text-2xl font-bold">
        <Flex align={'center'}>
          <IconFileZip size="2rem" />
          <span>Zipper</span>
        </Flex>
      </h1>
    </header>
  );
}
