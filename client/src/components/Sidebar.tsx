"use client"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { LayoutDashboard, Settings, Zap, MessageCircleQuestion, Plus } from "lucide-react"

function Sidebar() {
    return (
        <div className='flex flex-col h-1/3 justify-between bg-gradient-to-r from-violet-200 to-pink-200 shadow-lg h-full w-full rounded-l-lg py-8'>
            <div className="flex flex-row gap-2 justify-center items-center">
                <Zap className="" size={30} />
            </div>
            <div className="flex flex-col gap-8 items-center">
                <a className="mb-8 p-2 rounded-lg shadow-lg bg-gradient-to-r from-violet-100 to-pink-100  backdrop-blur-sm text-purple-300">
                    <Plus />
                </a>
                <LayoutDashboard />
                <Settings />
                <MessageCircleQuestion />
            </div>
            <div className="flex flex-row items-center justify-center">
                <Avatar>
                    <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
                    <AvatarFallback>CN</AvatarFallback>
                </Avatar>
            </div>
        </div>
    )
}

export default Sidebar