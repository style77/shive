import { Building, Copy, UsersRound } from "lucide-react"
import { AnimatedTooltip } from "@/components/ui/animated-tooltip";
import { motion } from "framer-motion";

const people = [
  {
    id: 1,
    name: "John Doe",
    designation: "Software Engineer",
    image:
      "https://images.unsplash.com/photo-1599566150163-29194dcaad36?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3387&q=80",
  },
  {
    id: 2,
    name: "Robert Johnson",
    designation: "Product Manager",
    image:
      "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 3,
    name: "Jane Smith",
    designation: "Data Scientist",
    image:
      "https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8YXZhdGFyfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 4,
    name: "Emily Davis",
    designation: "UX Designer",
    image:
      "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGF2YXRhcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 5,
    name: "Tyler Durden",
    designation: "Soap Developer",
    image:
      "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3540&q=80",
  },
  {
    id: 6,
    name: "Dora",
    designation: "The Explorer",
    image:
      "https://images.unsplash.com/photo-1544725176-7c40e5a71c5e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3534&q=80",
  },
];


function Card() {
  const waveVariants = {
    initial: { backgroundPositionY: '100%' },
    hover: { backgroundPositionY: '-32%' }
  };
  const heightVariants = {
    initial: { height: '0' },
    hover: { height: '100%' }
  }
  return (
    <motion.div
      className="flex flex-col relative justify-between bg-white border shadow-lg w-72 h-52 rounded-lg text-start z-0 hover:text-white hover:cursor-pointer transition delay-175"
      style={{ backgroundImage: 'url(wave.svg)', backgroundRepeat: 'no-repeat', backgroundPosition: 'bottom' }}
      variants={waveVariants}
      initial="initial"
      whileHover="hover"
      animate="rest">
      <motion.div
        className="absolute bottom-0 left-0 w-full bg-[#f6d0eb] -z-10"
        style={{
          height: 0
        }}
        variants={heightVariants}
      ></motion.div>
      <div className="flex flex-row gap-1 items-center p-4">
        <Building size={50} />
        <div className="flex flex-col">
          <h1 className="text-lg font-medium">Org name</h1>
          <a className="flex flex-row items-center font-light text-xs text-gray-400 gap-1">@org1-ease32-23432eas <a><Copy size={13} /></a></a>
        </div>
      </div>
      <div className="flex flex-row justify-between items-end py-2 px-4 text-white font-medium text-sm z-10">
        <a className="flex flex-row items-center gap-1"><UsersRound size={18} /> 5/16</a>
        <div className="flex flex-row gap-1 px-2">
          <AnimatedTooltip items={people} />
        </div>
      </div>
    </motion.div>
  )
}

export default Card