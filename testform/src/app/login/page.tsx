"use client"
import React, { useState } from "react";
import { NextPage } from "next";

interface LoginResponse {
  ok: boolean;
  statusText: string;
}

const Loginpage: NextPage = () => {
  const [username, setUsername] = useState<string>(""); 
  const [Contact_Number, setContact_Number] = useState<string>(""); 
  const [Age, setAge] = useState<number | null>(null); 
 

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:8000/api/v1/form/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            contact_number: Contact_Number,
            name: username,
            age: Age
        }),
      });

      if (response.ok) {
        console.log(response);

        setUsername("")
        setContact_Number("")
        setAge(0)
        window.location.href = "http://localhost:3000/showdata";
      } else {
        const responseData: LoginResponse = await response.json();
        console.error("Login failed:", responseData.statusText);
        alert("Login failed!");
      }
     
    } catch (error) {
      console.error("Error during login:", error);
    }
  };

  return (
    <div className="w-full h-auto mt-[16rem] flex justify-center">
      <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" onSubmit={handleLogin}>
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
            Username
          </label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="mb-6">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Contact Number">
          Contact Number
          </label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            id="Contact Number"
            type="text"
            placeholder="contact_number"
            value={Contact_Number}
            onChange={(e) => setContact_Number(e.target.value)}
          />
        </div>
        <div className="mt-[-1rem]">
          <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="Age">
          Age
          </label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            id="password"
            type="text"
            placeholder="Age"
            value={Age}
            onChange={(e) => {
                const value = e.target.value;
                const parsedAge = value === "" ? null : parseInt(value);
                setAge(parsedAge);
            }}

          />
        </div>
        <div className="grid justify-items-center">
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline "
            type="submit"
          >
            Submit
          </button>
        </div>
      <p className="text-center text-gray-500 text-xs mt-[1rem]">
        &copy;2024 Cogneo Technologies Pvt ltd. All rights reserved.
      </p>
      </form>
    </div>
  );
};

export default Loginpage;
