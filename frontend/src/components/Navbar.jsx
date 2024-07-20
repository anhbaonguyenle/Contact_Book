import { Container, Box, Flex, Link, Button, useColorMode, useColorModeValue,  } from "@chakra-ui/react"
import { IoMoon } from "react-icons/io5";
import { LuSun } from "react-icons/lu";

const Navbar = () => {
    const { colorMode, toggleColorMode } = useColorMode();
    return <Container maxW={"2000"}>
        <Box
        px={4}
        my={4}
        borderRadius={5}
        bg={useColorModeValue("gray.200", "gray.700")}
        >
            <Flex h="16"
            alignItems={"center"}
            justifyContent={"space-between"}>

                {/* Left side */}
                <Flex 
                alignItems={"center"}
                justifyContent={"center"}
                gap={3}
                display={{base: "none", sm: "flex"}}
                >
                    <Box><Link>Home</Link></Box>
                </Flex>
                {/* Center */}
                <Flex 
                alignItems={"center"}
                justifyContent={"center"}
                gap={3}
                display={{base: "none", sm: "flex"}}
                >
                    <Box><Link>search bar</Link></Box>
                    
                </Flex>
                {/* Right side */}
                <Flex            
                alignItems={"center"}
                justifyContent={"center"}
                gap={3}
                display={{base: "none", sm: "flex"}}>
                    <Box><Link>About</Link></Box>
                    <Button onClick={toggleColorMode}>
                                {colorMode === "light" ? <IoMoon /> : <LuSun size={20} />}
                            </Button>
                    <Box><Link>Login</Link></Box>
                    <Box><Link>Register</Link></Box>
                </Flex>
            
            </Flex>
        </Box>
    </Container>
    }

export default Navbar