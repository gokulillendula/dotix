import axios from "axios"

export const api = axios.create({
  baseURL: "https://dotix.onrender.com/api/"
})
