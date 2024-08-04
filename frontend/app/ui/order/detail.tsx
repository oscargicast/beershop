import { Order } from "@/app/lib/definitions";
import { formatDateToLocal } from "@/app/lib/utils";

export default function OrderDetail({ order }: { order: Order }) {
  return (
    <main>
      <h1 className="mb-4 text-xl md:text-2xl">
        Order Reference: <strong>{order.reference}</strong> 🍺
      </h1>
      <h2 className="mb-2 text-l md:text-xl">
        {formatDateToLocal(order.created)}
      </h2>
      <p className="mb-2 text-l md:text-xl">
        Is paid? {order.paid ? "✅" : "❌"}
      </p>
    </main>
  );
}
