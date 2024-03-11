import LoginForm from '@/components/LoginForm'
import RegisterForm from '@/components/RegisterForm'
import { useState } from 'react'
import { motion, AnimatePresence } from "framer-motion"

const container = {
    hidden: { opacity: 0 },
    show: { opacity: 1, transition: { ease: "linear", duration: 2 } }
};


function Login() {
    const [showRegister, setShowRegister] = useState(false)
    const handleToggle = () => {
        setShowRegister(showRegister);
    };
    return (
        <div className='w-full h-screen flex flex-col justify-center items-center background'>
            <div className='flex flex-col h-[60vh] w-96 justify-center bg-white shadow-xl rounded-lg p-16'>
                {/* {
                    showRegister ? (
                        <>
                            <RegisterForm />
                            <a className="text-sm text-start text-gray-400">Already have account? <span onClick={() => setShowRegister(false)} className="text-black font-medium">Login</span></a>
                        </>
                    ) : (
                        <>
                            <LoginForm />
                            <a className="text-sm text-start text-gray-400">Don't have an account? <span onClick={() => setShowRegister(true)} className="text-black font-medium">Register</span></a>
                        </>
                    )
                } */}
                <AnimatePresence mode='wait'>
                    {!showRegister ? (
                        <motion.div
                            key="visibleDiv"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                        >
                            <LoginForm />
                            <a className="text-sm text-start text-gray-400">You don't have an account? <span onClick={() => setShowRegister(true)} className="text-black font-medium">Register</span></a>
                        </motion.div>
                    ) : (
                        <motion.div
                        key="hiddenDiv"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        >
                            <RegisterForm />
                            <a className="text-sm text-start text-gray-400">Already have an account? <span onClick={() => setShowRegister(false)} className="text-black font-medium">Login</span></a>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </div>
    )
}

export default Login
