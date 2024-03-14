import Card from "@/components/Card"
import Sidebar from "@/components/Sidebar"

function Dashboard() {

    return (
        <div className='flex flex-row h-screen bg-white w-full'>
            <div className="flex flex-col py-6 px-16 w-full">
                <div className="flex flex-row justify-between w-full items=center">
                    <h1 className="text-3xl font-semibold">Welcome, Dominik</h1>
                </div>
                <div className="flex flex-row flex-wrap gap-8 rounded-lg w-full h-min-96 my-6">
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                </div>
            </div>
            <div className="flex w-[10vh] shadow-xl">
                <Sidebar />
            </div>
        </div>
    )
}

export default Dashboard