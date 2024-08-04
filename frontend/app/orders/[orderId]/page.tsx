import { fetchOrderById } from "@/app/lib/data";
import OrderItemsTable from "@/app/ui/order/table";
import OrderDetail from "@/app/ui/order/detail";
import { notFound } from "next/navigation";

export default async function OrderDetails({
  params,
}: {
  params: { orderId: string };
}) {
  try {
    const order = await fetchOrderById(params.orderId);
    return (
      <main>
        <OrderDetail order={order} />
        <OrderItemsTable order={order} />
      </main>
    );
  } catch (error) {
    notFound();
  }
}
