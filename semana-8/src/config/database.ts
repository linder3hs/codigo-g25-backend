import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export async function connectDB(): Promise<void> {
  try {
    await prisma.$connect();
    console.log("La connection fue exitosa!!!");
  } catch (error) {
    console.error(`Hubo un error ${error}`);
    process.exit(1);
  }
}

export async function disconnectDB(): Promise<void> {
  await prisma.$disconnect();
}

export default prisma;
