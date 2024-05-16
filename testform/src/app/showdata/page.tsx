"use client"
import React, { useState, useEffect } from "react";
import { NextPage } from "next";

const Showdata: NextPage = () => {
  const [showTable, setShowTable] = useState(false);
  const [responseData, setResponseData] = useState<any[][]>([]);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/v1/form/detail");
      const data = await response.json();
      setResponseData(data); 
      setShowTable(true);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const generateTable = (data: any[][]) => {
    return (
      <table className="w-full border-collapse border border-gray-400 mt-[5rem]" >
        <thead className="bg-gray-200">
          <tr>
            {data[0].map((header, index) => (
              <th key={index} className="px-4 py-2">{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.slice(1).map((rowData, index) => (
            <tr key={index}>
              {rowData.map((cellData, cellIndex) => (
                <td key={cellIndex} className="border px-4 py-2">{cellData}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  return (
    <div className="flex flex-col items-center mt-8">
      <button onClick={fetchData} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ">
        Show Data
      </button>
      {showTable && generateTable(responseData)}
    </div>
  );
};

export default Showdata;
