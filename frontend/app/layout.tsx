import type { Metadata } from "next";
import { robotoCondensed } from "./ui/fonts";
import "./globals.css";

export const metadata: Metadata = {
  title: "Beershop",
  description: "Demo",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={robotoCondensed.className}>{children}</body>
    </html>
  );
}
