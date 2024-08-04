/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/orders/',
        permanent: true, // Use false for a temporary redirect (e.g., 302)
      },
    ];
  },
};

export default nextConfig;
