import { Order } from "@/app/lib/definitions";

export async function fetchOrderById(id: string): Promise<Order> {
  try {
    const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
    if (!apiUrl) {
      throw new Error("API base URL is not defined.");
    }
    const url = `${apiUrl}/api/v1/orders/${id}`;
    const res = await fetch(url);
    if (!res.ok) {
      throw new Error(`Error fetching order: ${res.status}`);
    }
    const json = await res.json();
    return json as Order;
  } catch (error) {
    console.error("API Error:", error);
    throw new Error(`Failed to fetch order: ${id}`);
  }
}
