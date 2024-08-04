export type OrderItem = {
  name: string;
  price_per_unit: number;
  total: number; // quantity
};

export type Order = {
  reference: string;
  created: string;
  taxes: number;
  discount: number;
  subtotal: number;
  paid: boolean;
  items: OrderItem[];
};
