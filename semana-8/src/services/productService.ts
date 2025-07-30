import prisma from "../config/database";
import type { CreateProductRequest, UpdateProductRequest } from "../types";

export class ProductService {
  static async getAllProduct(
    page: number = 1,
    limit: number = 10,
    search?: string
  ) {
    const skip = (page - 1) * limit;

    const where: any = {};

    if (search) {
      where.OR = [
        { name: { contains: search, mode: "insensitive" } },
        { description: { contains: search, mode: "insensitive" } },
      ];
    }

    const [products, total] = await Promise.all([
      prisma.product.findMany({
        where,
        include: {
          category: true,
        },
        orderBy: { createdAt: "desc" },
        skip,
        take: limit,
      }),
      prisma.product.count({ where }),
    ]);

    return {
      products,
      pagination: {
        total,
        page,
        limit,
        totalPage: Math.ceil(total / limit),
      },
    };
  }

  static async getProductById(id: number) {
    return await prisma.product.findUnique({ where: { id } });
  }

  static async createProduct(data: CreateProductRequest) {
    return await prisma.product.create({
      data,
    });
  }

  static async updateProduct(id: number, data: UpdateProductRequest) {
    const product = await prisma.product.findUnique({ where: { id } });

    if (!product) return false;

    return await prisma.product.update({
      where: { id },
      data,
    });
  }

  static async deleteProduct(id: number) {
    return await prisma.product.delete({ where: { id } });
  }
}
