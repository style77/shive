"use client";
import {
  useMotionValue,
} from "framer-motion";

export const AnimatedTooltip = ({
  items,
}: {
  items: {
    id: number;
    image: string;
  }[];
}) => {
  const x = useMotionValue(0); // going to set this value on mouse move
  // rotate the tooltip
  const handleMouseMove = (event: any) => {
    const halfWidth = event.target.offsetWidth / 2;
    x.set(event.nativeEvent.offsetX - halfWidth); // set the x value, which is then used in transform and rotate
  };

  return (
    <>
      {items.map((item) => (
        <div
          className="-mr-4 relative group"
          key={item.id}
        >
          <img
            onMouseMove={handleMouseMove}
            height={100}
            width={100}
            src={item.image}
            className="object-cover !m-0 !p-0 hover:!mr-2 transition object-top rounded-full h-7 w-7 border-2 group-hover:scale-105 border-white relative transition duration-500"
          />
        </div>
      ))}
    </>
  );
};