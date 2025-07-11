import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";

export function Register() {
  return (
    <Card className="w-full max-w-md mx-auto mt-5">
      <CardHeader>
        <CardTitle className="text-2xl font-bold">
          Registrate en nuestra web
        </CardTitle>
        <CardDescription>Crea una cuenta y valida tu correo</CardDescription>
      </CardHeader>
      <CardContent>
        <form className="flex flex-col gap-5">
          <div>
            <Input
              type="text"
              name="username"
              placeholder="Escribe tu username"
            />
          </div>
          <div>
            <Input
              type="email"
              name="email"
              placeholder="Escribe tu correo electronico"
            />
          </div>
          <div>
            <Input
              type="password"
              name="password"
              placeholder="Escribe tu password"
            />
          </div>
          <div>
            <Input
              type="password"
              name="password_confirm"
              placeholder="Verifica tu password"
            />
          </div>
          <div>
            <Input
              type="text"
              name="first_name"
              placeholder="Escribe tu nombre"
            />
          </div>
          <div>
            <Input
              type="text"
              name="last_name"
              placeholder="Escribe tu apellido"
            />
          </div>
          <Button type="submit">Crear Cuenta</Button>
        </form>
      </CardContent>
    </Card>
  );
}
