<template>
  <!-- Content -->
  <div class="w-full md:w-1/2">
    <div class="min-h-[100dvh] h-full flex flex-col after:flex-1">
      <div class="max-w-sm mx-auto w-full px-4 py-8">
        <h1 class="text-3xl text-gray-800 dark:text-gray-100 font-bold mb-6">Sign In</h1>
        <!-- Form -->
        <form>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium mb-1" for="email">Email Place</label>
              <input id="email" class="form-input w-full" type="email" v-model="email" />
            </div>
            <div>
              <label class="block text-sm font-medium mb-1" for="password">Password</label>
              <div class="relative mt-2 flex">
                <input
                    v-model="password"
                    ref="password_input"
                    id="password"
                    name="password"
                    :type="password_input_type"
                    autocomplete="on"
                    required="true"
                    class="form-input w-full"
                />
                <div class="absolute right-4 flex h-full items-center">
                  <svg
                      @click="togglePasswordVisibility()"
                      v-if="password_input_type === 'password'"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke-width="1.5"
                      stroke="currentColor"
                      class="size-5"
                  >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M3.98 8.223A10.477 10.477 0 0 0 1.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.451 10.451 0 0 1 12 4.5c4.756 0 8.773 3.162 10.065 7.498a10.522 10.522 0 0 1-4.293 5.774M6.228 6.228 3 3m3.228 3.228 3.65 3.65m7.894 7.894L21 21m-3.228-3.228-3.65-3.65m0 0a3 3 0 1 0-4.243-4.243m4.242 4.242L9.88 9.88"
                    />
                  </svg>
                  <svg
                      @click="togglePasswordVisibility()"
                      v-else
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke-width="1.5"
                      stroke="currentColor"
                      class="size-5"
                  >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z"
                    />
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-between mt-6">
            <div class="mr-1">
              <router-link class="text-sm hover:no-underline text-blue-600" to="/reset-password">Forgot Password?</router-link>
            </div>
            <div class="btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-white whitespace-nowrap ml-3"
                 @click="handleSignIn">Sign In</div>
          </div>
        </form>
        <!-- Footer -->
        <div class="pt-5 mt-6 border-t border-gray-200 dark:border-gray-700">
          <div class="text-sm">
            Don’t you have an account? <router-link class="font-medium text-blue-600 hover:text-violet-600 dark:hover:text-violet-400" to="/signup">Sign Up</router-link>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/UserStore.ts";

const userStore = useUserStore();
const router = useRouter();

const email = ref("")
const password = ref("")

const password_input = ref<HTMLInputElement | null>(null)
const password_input_type = ref<string>('password')
function togglePasswordVisibility() {
  if (password_input.value != null) {
    if (password_input_type.value === 'password') {
      password_input_type.value = 'text'
      password_input.value.focus()
    } else {
      password_input_type.value = 'password'
      password_input.value.focus()
    }
  }
}
function validateSignInForm () {
  return (password.value.trim() != "" && email.value.trim() != "");
}
function handleSignIn() {
  // if (validateSignInForm()) {
  //   userStore.signIn(email.value, password.value).then((state) => {
  //     validateUserAuthentication(state)
  //   })
  // } else {
  // }
  router.push('/dashboard')
}


async function validateUserAuthentication(state: string) {
  if (state === "CONNECTED" || state === "USER_IDENTIFIED" || state === "USER_CREATED") {
    setTimeout(() => router.push('/dashboard'),800)
  } else if (state === "INVALID_CREDENTIALS") {
  } else {
  }
}
</script>