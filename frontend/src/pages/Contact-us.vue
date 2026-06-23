<template>

  <!-- <section class="relative h-[280px] sm:h-[450px] overflow-hidden"> -->
  <!-- Banner Section -->

  <section class="mb-0 md:mb-4">
    <img src="/files/contactbanner (2).png" alt="Contact Us"
      class="w-full h-[250px] object-contain md:h-[450px] md:object-cover" />
  </section>






  <section class="mb-14 ">
    <div class="pt-12 max-w-6xl mx-auto px-2 sm:px-6 lg:px-8">

      <!-- Main Section -->
      <div class="grid lg:grid-cols-2 gap-10">

        <!-- Left Image -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

          <!-- Address -->
          <div
            class="bg-[#FFF8E7] rounded-lg p-2 shadow-md hover:shadow-xl transition flex flex-col items-center justify-center text-center">
            <div class="w-16 h-16 mx-auto rounded-xl bg-orange-50 flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-orange-500 text-3xl">
                location_on
              </span>
            </div>

            <h3 class="text-xl font-semibold text-[#2f2f68] mb-2">
              Address
            </h3>

            <p class="text-gray-500">
              Bangalore, Karnataka, India
            </p>
          </div>

          <!-- Contact -->
          <div
            class="bg-white rounded-lg p-2 shadow-md hover:shadow-xl transition flex flex-col items-center justify-center text-center">
            <div class="w-16 h-16 mx-auto rounded-xl bg-cyan-50 flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-cyan-600 text-3xl">
                call
              </span>
            </div>

            <h3 class="text-xl font-semibold text-[#2f2f68] mb-2">
              Contact
            </h3>

            <p class="text-gray-500">
              +91 9686872201
            </p>
          </div>

          <!-- Email -->
          <div
            class="bg-white rounded-lg p-2 shadow-md hover:shadow-xl transition flex flex-col items-center justify-center text-center">
            <div class="w-16 h-16 mx-auto rounded-xl bg-green-50 flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-green-600 text-3xl">
                mail
              </span>
            </div>

            <h3 class="text-xl font-semibold text-[#2f2f68] mb-2">
              Email
            </h3>

            <p class="text-gray-500 break-all">
              info@persquarefeet.com
            </p>
          </div>

          <!-- Map -->
          <div
            class="bg-[#FFF8E7] rounded-lg p-2 shadow-md hover:shadow-xl transition flex flex-col items-center justify-center text-center">

            <div class="w-16 h-16 rounded-xl bg-pink-50 flex items-center justify-center mb-5">
              <span class="material-symbols-outlined text-pink-600 text-3xl">
                map
              </span>
            </div>

            <h3 class="text-xl font-semibold text-[#2f2f68] mb-2">
              Google Map
            </h3>

            <a href="#" class="text-indigo-600 hover:text-indigo-700">
              View Location
            </a>

          </div>

        </div>

        <!-- Right Form -->
        <!-- Right Side Form -->
        <div class="bg-[#FFF8E7] rounded-[30px] shadow-xl p-6 sm:p-6">

          <h2 class="text-4xl font-bold text-[#2f2f68] mb-2">
            Send us a message
          </h2>

          <p class="text-gray-500 text-lg leading-6 mb-6">
            Your satisfaction is our top priority, and we are committed to
            providing exceptional service and support.
          </p>

          <form @submit.prevent="submitForm" class="space-y-3">

            <!-- Name -->
            <div>
              <label class="block text-gray-700 font-medium mb-2">
                Your Name <span class="text-red-500">*</span>
              </label>

              <input v-model="form.name" type="text" placeholder="Enter your name"
                class="w-full h-10 px-5 border border-gray-300 rounded-xl outline-none focus:border-[#0B1560]"
                required />
            </div>

            <!-- Email -->
            <div>
              <label class="block text-gray-700 font-medium mb-2">
                Email Address <span class="text-red-500">*</span>
              </label>

              <input v-model="form.email" type="email" placeholder="Enter your email"
                class="w-full h-10 px-5 border border-gray-300 rounded-xl outline-none focus:border-[#0B1560]"
                required />
            </div>

            <!-- Phone -->
            <div>
              <label class="block text-gray-700 font-medium mb-2">
                Phone Number <span class="text-red-500">*</span>
              </label>

              <input v-model="form.phone" type="text" placeholder="Enter your phone number"
                class="w-full h-10 px-5 border border-gray-300 rounded-xl outline-none focus:border-[#0B1560]"
                required />
            </div>

            <!-- Service -->
            <div>
              <label class="block text-gray-700 font-medium mb-2">
                Select Service
              </label>

              <select class="w-full h-10 px-5 border border-gray-300 rounded-xl outline-none focus:border-[#0B1560]">
                <option>Select Service</option>
                <option>Real Estate Consultation</option>
                <option>Housing Loan Services</option>
                <option>Interior Design Services</option>
                <option>Legal Consultation</option>
                <option>Property Management</option>
                <option>Construction Services</option>
              </select>
            </div>

            <!-- Message -->
            <!-- <div>
              <label class="block text-gray-700 font-medium mb-2">
                Message
              </label>

              <textarea rows="5" placeholder="Write your message..."
                class="w-full border border-gray-300 rounded-xl px-5 py-4 outline-none focus:border-[#0B1560]"></textarea>
            </div> -->

            <!-- Submit -->
            <button type="submit"
              class="w-full h-10 bg-[#0B1560] hover:bg-[#16248f] text-white rounded-xl font-semibold transition">
              Send Message
            </button>

          </form>

          <!-- Success -->
          <p v-if="successMessage" class="mt-4 text-green-600 text-center font-medium">
            Your message has been submitted successfully.
          </p>

          <!-- Error -->
          <p v-if="errorMessage" class="mt-4 text-red-600 text-center font-medium">
            {{ errorText }}
          </p>

        </div>

      </div>







    </div>
  </section>






  <!-- Map Section -->
  <section class="px-4  sm:px-6 lg:px-10 pb-6">

    <div class="max-w-7xl mx-auto">

      <div class="rounded-[30px] overflow-hidden shadow-lg">

        <iframe src="https://www.google.com/maps?q=Quantumberg+Technologies+Bangalore&output=embed" width="100%"
          height="450" style="border:0;" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

      </div>

    </div>

  </section>

</template>


<script setup>

// import { reactive, ref } from "vue";

// const successMessage=ref(false)
// const errorMessage = ref(false);

// const form = reactive({
//   name: "",
//   email: "",
//   phone: "",
//   // service: "",
//   // message: "",
// });

// const submitForm = async () => {
//   try {

//     const response = await fetch(
//       "/api/method/per_sqr_ft.api.lead.add_lead",
//       {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },

//         body: JSON.stringify({
//           name: form.name,
//           phone: form.phone,
//           email: form.email,
//           // mobile_no: form.phone,
//           // service: form.service,
//           // message: form.message,
//         }),
//       }
//     );

//     const data = await response.json();

//     if (data.message === "Lead added successfully") {


//      successMessage.value = true;

// setTimeout(() => {
//   successMessage.value = false;
// }, 4000);


//       form.name = "";
//       form.phone = "";
//       form.email = "";

//       // form.service = "";
//       // form.message = "";
//     }
//     else {

//   errorMessage.value = true;

//   setTimeout(() => {
//     errorMessage.value = false;
//   }, 4000);

// }

//   } catch (error) {

//     console.error(error);
//     alert("Something went wrong");

//   }
// };

import { reactive, ref } from "vue";

const successMessage = ref(false);
const errorMessage = ref(false);
const errorText = ref("");

const form = reactive({
  name: "",
  email: "",
  phone: "",
});

const submitForm = async () => {
  // Frontend validations
  if (!form.name.trim()) {
    errorText.value = "Name is required";
    errorMessage.value = true;

    setTimeout(() => {
      errorMessage.value = false;
    }, 4000);

    return;
  }

  if (!form.email.trim()) {
    errorText.value = "Email is required";
    errorMessage.value = true;

    setTimeout(() => {
      errorMessage.value = false;
    }, 4000);

    return;
  }

  if (!form.phone.trim()) {
    errorText.value = "Phone number is required";
    errorMessage.value = true;

    setTimeout(() => {
      errorMessage.value = false;
    }, 4000);

    return;
  }

  try {
    const response = await fetch(
      "/api/method/per_sqr_ft.api.lead.add_lead",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: form.name,
          email: form.email,
          phone: form.phone,
        }),
      }
    );

    const data = await response.json();
    // const data = await response.json();

    console.log("Response Status:", response.status);
    console.log("Response Data:", data);

    // Backend validation errors
    if (data.exc) {
      errorText.value = "Email or Phone already exists";
      errorMessage.value = true;

      setTimeout(() => {
        errorMessage.value = false;
      }, 4000);

      return;
    }

    if (data.message === "Lead added successfully") {
      successMessage.value = true;

      setTimeout(() => {
        successMessage.value = false;
      }, 4000);

      // Clear form
      form.name = "";
      form.email = "";
      form.phone = "";
    }
  } catch (error) {
    console.error(error);

    errorText.value = "Something went wrong";
    errorMessage.value = true;

    setTimeout(() => {
      errorMessage.value = false;
    }, 4000);

    if (!/^\d{10}$/.test(form.phone)) {
      errorText.value = "Phone number must contain exactly 10 digits";
      errorMessage.value = true;

      setTimeout(() => {
        errorMessage.value = false;
      }, 4000);

      return;
    }
  }
};

</script>