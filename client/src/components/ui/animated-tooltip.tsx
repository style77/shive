"use client";
import {
  useMotionValue,
} from "framer-motion";
import { MouseEvent } from "react";

export const AnimatedTooltip = ({
  items,
}: {
  items: {
    id: number;
    image: string;
  }[];
}) => {
  const x = useMotionValue(0);
  const handleMouseMove = (event: MouseEvent<HTMLImageElement>) => {
    const target = event.target as HTMLImageElement;
    const halfWidth = target.offsetWidth / 2;

    x.set(event.nativeEvent.offsetX - halfWidth);
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