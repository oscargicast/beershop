import { Order, OrderItem } from "@/app/lib/definitions";
import { formatCurrency } from "@/app/lib/utils";

export default async function OrderItemsTable({ order }: { order: Order }) {
  const orderItems = order.items;
  return (
    <div className="mt-6 flow-root">
      <div className="inline-block min-w-full align-middle">
        <div className="rounded-lg bg-gray-50 p-2 md:pt-0">
          <table className="hidden min-w-full text-gray-900 md:table">
            <thead className="rounded-lg text-left text-sm font-normal">
              <tr>
                <th scope="col" className="px-4 py-5 font-medium sm:pl-6">
                  Beer
                </th>
                <th scope="col" className="px-3 py-5 font-medium">
                  Qty
                </th>
                <th scope="col" className="px-3 py-5 font-medium">
                  Unit Price
                </th>
                <th scope="col" className="px-3 py-5 font-medium">
                  Subtotal
                </th>
              </tr>
            </thead>
            <tbody className="bg-white">
              {orderItems?.map((orderItem: OrderItem) => (
                <tr
                  key={orderItem.name}
                  className="w-full border-b py-3 text-sm last-of-type:border-none [&:first-child>td:first-child]:rounded-tl-lg [&:first-child>td:last-child]:rounded-tr-lg [&:last-child>td:first-child]:rounded-bl-lg [&:last-child>td:last-child]:rounded-br-lg"
                >
                  <td className="whitespace-nowrap py-3 pl-6 pr-3">
                    <div className="flex items-center gap-3">
                      <p>{orderItem.name}</p>
                    </div>
                  </td>
                  <td className="whitespace-nowrap px-3 py-3">
                    {orderItem.total}
                  </td>
                  <td className="whitespace-nowrap px-3 py-3">
                    {formatCurrency(orderItem.price_per_unit)}
                  </td>
                  <td className="whitespace-nowrap px-3 py-3">
                    {formatCurrency(orderItem.total * orderItem.price_per_unit)}
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot className="bg-gray-200">
              <tr>
                <td className="whitespace-nowrap py-3 pl-6 pr-3"></td>
                <td className="whitespace-nowrap px-3 py-3"></td>
                <td className="whitespace-nowrap px-3 py-3 font-bold">
                  IVA: 19%
                </td>
                <td className="whitespace-nowrap px-3 py-3">
                  {formatCurrency(order.taxes)}
                </td>
              </tr>
              <tr>
                <td className="whitespace-nowrap py-3 pl-6 pr-3"></td>
                <td className="whitespace-nowrap px-3 py-3"></td>
                <td className="whitespace-nowrap px-3 py-3 font-bold">Total</td>
                <td className="whitespace-nowrap px-3 py-3 font-bold">
                  {formatCurrency(order.subtotal)}
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  );
}
