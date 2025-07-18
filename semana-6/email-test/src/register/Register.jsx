"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { singUp } from "@/service/fetching";

export function Register() {
  const [inputs, setInputs] = useState({
    username: "",
    email: "",
    password: "",
    password_confirm: "",
    first_name: "",
    last_name: "",
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    setInputs({
      ...inputs,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await singUp(inputs);

      if (!response.ok) {
        const error = JSON.stringify(await response.json(), null, 2);
        alert(error);
        return;
      }
      alert(
        "La cuenta fue creada exitosamente, revisa tu correo para activarla."
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Card className="w-full max-w-md mx-auto mt-5">
      <CardHeader>
        <CardTitle className="text-2xl font-bold">
          Registrate en nuestra web
        </CardTitle>
        <CardDescription>Crea una cuenta y valida tu correo</CardDescription>
      </CardHeader>
      <CardContent>
        <form className="flex flex-col gap-5" onSubmit={handleSubmit}>
          <div className="grid gap-2">
            <Label htmlFor="username">Username</Label>
            <Input
              id="username"
              type="text"
              name="username"
              placeholder="Escribe tu username"
              required
              onChange={handleInputChange}
              value={inputs.username}
            />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              name="email"
              placeholder="Escribe tu correo electronico"
              required
              onChange={handleInputChange}
              value={inputs.email}
            />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="password">Contraseña</Label>
            <Input
              id="password"
              type="password"
              name="password"
              placeholder="Escribe tu password"
              required
              onChange={handleInputChange}
              value={inputs.password}
            />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="password_confirm">Verifica tu contraseña</Label>
            <Input
              id="password_confirm"
              type="password"
              name="password_confirm"
              placeholder="Verifica tu password"
              required
              onChange={handleInputChange}
              value={inputs.password_confirm}
            />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="first_name">Nombre</Label>
            <Input
              id="first_name"
              type="text"
              name="first_name"
              placeholder="Escribe tu nombre"
              required
              onChange={handleInputChange}
              value={inputs.first_name}
            />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="last_name">Apellido</Label>
            <Input
              id="last_name"
              type="text"
              name="last_name"
              placeholder="Escribe tu apellido"
              required
              onChange={handleInputChange}
              value={inputs.last_name}
            />
          </div>
          <Button type="submit">Crear Cuenta</Button>
        </form>
      </CardContent>
    </Card>
  );
}
