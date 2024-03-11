"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { PasswordInput } from "@/components/ui/password-input"
import { useState } from "react"
import { Separator } from "@/components/ui/separator"
import google from "../assets/google.svg"
import github from "../assets/github.svg"

const formSchema = z.object({
  email: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
  password: z.string().min(8, {
    message: "Password must be at least 8 characters."
  }),
})

function LoginForm() {
  const [currentPassword, setCurrentPassword] = useState("")

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
    },
  })

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values)
  }
  return (
    <div className='flex text-start justify-center flex-col'>
      <div className="flex flex-col gap-1 pb-4">
        <h1 className="text-3xl font-semibold">Welcome back</h1>
        <p className="text-sm text-gray-400">Please enter your login details to continue.</p>
      </div>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormControl>
                  <Input placeholder="Email address" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormControl>
                  <PasswordInput
                    id="current_password"
                    value={currentPassword}
                    onChange={(e) => setCurrentPassword(e.target.value)}
                    autoComplete="current-password"
                    placeholder="Password"
                  />
                </FormControl>
                <FormMessage />
                <a className="font-semibold text-black text-xs pl-1">Forgot your password?</a>
              </FormItem>
            )}
          />
          <div className="flex flex-col gap-4">
            <Button className="font-medium" type="submit">Login</Button>
          </div>
          <div className="flex flex-row items-center justify-center gap-3 w-60">
            <Separator />
            <h1 className="text-sm text-gray-400">Or</h1>
            <Separator />
          </div>
          <div className="flex flex-col gap-4 pb-2">
            <Button className="bg-white text-black border border-primary hover:text-white">
              <img src={github} className="mr-2 h-4 w-4" /> Login with Github
            </Button>
            <Button className="bg-white text-black border border-primary hover:text-white">
              <img src={google} className="mr-2 h-4 w-4" /> Login with Google
            </Button>
          </div>
        </form>
      </Form>
    </div>
  )
}

export default LoginForm