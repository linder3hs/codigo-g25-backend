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
    const product = await prisma.product.create({
      data,
    });

    return product;
  }

  static async deleteProduct(id: number) {
    return await prisma.product.delete({ where: { id } });
  }
}
