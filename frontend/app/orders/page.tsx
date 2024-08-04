import { Order } from "@/app/lib/definitions";
import { formatDateToLocal } from "@/app/lib/utils";

export default function OrderDetail({ order }: { order: Order }) {
  return (
    <main>
      <h1 className="mb-4 text-xl md:text-2xl">🍺 Beershop</h1>
    </main>
  );
}
