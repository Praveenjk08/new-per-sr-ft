<template>

  <!-- Banner Section -->
  <section class="px-4 sm:px-6 lg:px-10 my-8">

    <div
      class="relative w-full h-[300px] sm:h-[500px] lg:h-[600px] overflow-hidden rounded-[40px]"
    >

      <!-- Banner Image -->
      <img
        src="/files/contactbanner.png"
        alt="Contact Us"
        class="w-full h-full object-cover"
      />

      <!-- Overlay -->
      <div class="absolute inset-0 bg-black/45 rounded-[40px]"></div>

      <!-- Content -->
      <div
        class="absolute inset-0 flex flex-col items-center justify-center text-center px-6"
      >

        <h1
          class="text-white text-3xl sm:text-3xl lg:text-3xl font-bold leading-tight"
        >
          Contact Us
        </h1>

        <p
          class="text-white/90 text-sm sm:text-lg lg:text-xl mt-5 max-w-3xl leading-8"
        >
          We are here to help you with all your real estate,
          construction, interior, and property-related needs.
        </p>

      </div>

    </div>

  </section>


  <!-- Contact Section -->
  <section class="py-16 px-4 sm:px-6 lg:px-10">

    <div
      class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12"
    >

     <!-- Left Side Contact Card -->
<div
  class="bg-white rounded-[30px] shadow-xl p-4 sm:p-8 lg:p-10 h-fit"
>

  <!-- Heading -->
  <p
    class="text-[#4b4b9b] font-semibold text-base sm:text-lg mb-3 tracking-wide"
  >
    Get In Touch
  </p>

  <h2
    class="text-2xl sm:text-3xl font-bold text-[#2f2f68] leading-tight mb-6"
  >
    Let’s Discuss Your Dream Project
  </h2>

  <p
    class="text-gray-600 text-sm sm:text-base leading-8 mb-10"
  >
    Have questions about real estate, construction, interiors,
    or property management? Our expert team is here to help
    you with trusted guidance and professional support.
  </p>

  <!-- Contact Items -->
  <div class="space-y-5">

    <!-- Address -->
    <div
      class="flex items-start gap-4 border border-gray-100 rounded-2xl p-5 hover:shadow-lg transition duration-300"
    >

      <div
        class="min-w-[50px] h-[50px] rounded-xl bg-[#0B1560] text-white flex items-center justify-center text-xl"
      >
        📍
      </div>

      <div>
        <h3
          class="text-lg sm:text-xl font-semibold text-[#2f2f68] mb-1"
        >
          Office Address
        </h3>

        <p class="text-gray-600 leading-7 text-sm sm:text-base">
          Per Square Feet,<br />
          Bangalore, Karnataka, India
        </p>
      </div>

    </div>

    <!-- Phone -->
    <div
      class="flex items-start gap-4 border border-gray-100 rounded-2xl p-5 hover:shadow-lg transition duration-300"
    >

      <div
        class="min-w-[50px] h-[50px] rounded-xl bg-[#0B1560] text-white flex items-center justify-center text-xl"
      >
        📞
      </div>

      <div>
        <h3
          class="text-lg sm:text-xl font-semibold text-[#2f2f68] mb-1"
        >
          Call Us
        </h3>

        <p class="text-gray-600 leading-7 text-sm sm:text-base">
          +91 9686872201
        </p>
        <p class="text-gray-600 leading-7 text-sm sm:text-base">
          +91 8884436688
        </p>
      </div>

    </div>

    <!-- Email -->
    <div
      class="flex items-start gap-4 border border-gray-100 rounded-2xl p-5 hover:shadow-lg transition duration-300"
    >

      <div
        class="min-w-[50px] h-[50px] rounded-xl bg-[#0B1560] text-white flex items-center justify-center text-xl"
      >
        ✉️
      </div>

      <div>
        <h3
          class="text-lg sm:text-xl font-semibold text-[#2f2f68] mb-1"
        >
          Email Address
        </h3>

        <p class="text-gray-600 leading-7 text-sm sm:text-base">
          kenchagowda.gj@gmail.com
        </p>
      </div>

    </div>

    <!-- Timing -->
    <div
      class="flex items-start gap-4 border border-gray-100 rounded-2xl p-5 hover:shadow-lg transition duration-300"
    >

      <div
        class="min-w-[50px] h-[50px] rounded-xl bg-[#0B1560] text-white flex items-center justify-center text-xl"
      >
        ⏰
      </div>

      <div>
        <h3
          class="text-lg sm:text-xl font-semibold text-[#2f2f68] mb-1"
        >
          Working Hours
        </h3>

        <p class="text-gray-600 leading-7 text-sm sm:text-base">
          Monday - Saturday <br />
          9:00 AM - 7:00 PM
        </p>
      </div>

    </div>

  </div>

</div>


      <!-- Right Side Form -->
     <div
    class="bg-white rounded-[30px] shadow-xl p-8 sm:p-10"
  >

    <h2
      class="text-3xl font-bold text-[#2f2f68] mb-8"
    >
      Send Message
    </h2>

    <form
      class="space-y-6"
      @submit.prevent="submitForm"
    >

      <!-- Name -->
      <div>
        <input
          v-model="form.full_name"
          type="text"
          placeholder="Your Name"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        />
      </div>

      <!-- Email -->
      <div>
        <input
          v-model="form.email"
          type="email"
          placeholder="Your Email"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        />
      </div>

      <!-- Phone -->
      <div>
        <input
          v-model="form.phone_number"
          type="text"
          placeholder="Phone Number"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        />
      </div>

      <!-- Service -->
      <div>
        <select
          v-model="form.service"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        >
          <option value="">Select Service</option>
          <option>Real Estate Consultation</option>
          <option>Housing Loan Services</option>
          <option>Interior Design Services</option>
          <option>Legal Consultation</option>
          <option>Property Management</option>
          <option>Construction Services</option>
        </select>
      </div>

      <!-- Message -->
      <div>
        <textarea
          v-model="form.message"
          rows="5"
          placeholder="Write Your Message"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        ></textarea>
      </div>

      <!-- Button -->
      <button
        type="submit"
        class="w-full bg-[#0B1560] hover:bg-[#16248f] text-white py-4 rounded-2xl text-lg font-semibold transition duration-300"
      >
        Send Message
      </button>

    </form>

    
    
<p
  v-if="successMessage"
  class="text-green-600 text-center font-medium mt-4"
>
  Your message has been submitted successfully.
</p>

<p
  v-if="errorMessage"
  class="text-red-600 text-center font-medium mt-4"
>
  This email is already registered.
</p>

  </div>

    </div>

  </section>


  <!-- Map Section -->
<section class="px-4 sm:px-6 lg:px-10 pb-16">

  <div class="max-w-7xl mx-auto">

    <div class="rounded-[30px] overflow-hidden shadow-lg">

      <iframe
        src="https://www.google.com/maps?q=Quantumberg+Technologies+Bangalore&output=embed"
        width="100%"
        height="450"
        style="border:0;"
    
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>

    </div>

  </div>

</section>

</template>


<script setup>

import { reactive, ref } from "vue";

const successMessage=ref(false)
const errorMessage = ref(false);

const form = reactive({
  full_name: "",
  email: "",
  phone_number: "",
  service: "",
  message: "",
});

const submitForm = async () => {
  try {

    const response = await fetch(
      "/api/method/per_sqr_ft.api.contact.create_contact",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          full_name: form.full_name,
          email: form.email,
          phone_number: form.phone_number,
          service: form.service,
          message: form.message,
        }),
      }
    );

    const data = await response.json();

    if (data.message.status === "success") {

     
     successMessage.value = true;

setTimeout(() => {
  successMessage.value = false;
}, 4000);
      

      form.full_name = "";
      form.email = "";
      form.phone_number = "";
      form.service = "";
      form.message = "";
    }
    else {

  errorMessage.value = true;

  setTimeout(() => {
    errorMessage.value = false;
  }, 4000);

}

  } catch (error) {

    console.error(error);
    alert("Something went wrong");

  }
};
</script>