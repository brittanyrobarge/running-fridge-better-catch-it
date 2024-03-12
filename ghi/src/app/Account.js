import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const accountApi = createApi({
    reducerPath: 'account',
    baseQuery: fetchBaseQuery({
        baseUrl: import.meta.env.VITE_API_HOST,
        credentials: 'include',
    }),
    endpoints: (builder) => ({
        createAccount: builder.mutation({
            query: (info) => {
                const formData = new FormData()
                formData.append('name', info.name)
                formData.append('username', info.username)
                formData.append('password', info.password)
                formData.append('email', info.email)

                return {
                    url: '/pages/signUp',
                    method: 'POST',
                    body: formData,
                    credentials: 'include',
                }
            },
        }),
        login: builder.mutation({
            query: (body) => ({
                url: '/token',
                method: 'POST',
                body,
                credentials: 'include',
            }),
            // You might need to adjust the following line based on your actual response structure
            // The invalidatesTags property is used to invalidate the cache for a specific tag
            invalidatesTags: ['Account'],
        }),
        logout: builder.mutation({
            query: () => ({
                url: '/token',
                method: 'DELETE',
            }),
            invalidatesTags: ['Account'],
        }),
        getToken: builder.query({
            query: () => ({
                url: '/token',
            }),
            providesTags: ['Account'],
        }),
    }),
})

export const {
    useCreateAccountMutation,
    useLoginMutation,
    useLogoutMutation,
    useGetTokenQuery,
} = accountApi
