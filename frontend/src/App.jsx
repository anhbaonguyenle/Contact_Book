import { Button, Container, Stack } from "@chakra-ui/react"
import Navbar from "./components/Navbar"

function App() {
  return (
    <Stack minH={"100vh"}>
      <Navbar />
      <Container>
        <Button colorScheme="blue">Button</Button>
      </Container>
    </Stack>
  )
}

export default App
