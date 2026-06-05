<template>

  <section class="relative h-[280px] sm:h-[450px] overflow-hidden">
<div class="w-full  " >
  <img
    src="/files/contactbanner.png"
    alt="Contact Us"
    class="w-full h-[250px] sm:h-[450px] object-cover"
  />
</div>
 

  <div class="absolute inset-0 bg-black/55"></div>

  <div
    class="absolute inset-0 flex items-center justify-center"
  >

    <div class="text-center px-4">

      <!-- <h1
        class="text-white text-5xl md:text-7xl font-bold"
      >
        Let's Connect
      </h1> -->

      <!-- <p
        class="text-white/90 text-lg md:text-xl mt-6 max-w-3xl mx-auto"
      >
        Whether you're buying, selling, investing,
        or seeking property consultation,
        our experts are here to help.
      </p> -->

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
    class="text-[#4b4b9b]text-2xl sm:text-3xl  font-bold text-base mb-3 tracking-wide"
  >
    Get In Touch
  </p>

  <h2
    class=" sm:text-lg font-semibold text-[#2f2f68] leading-tight mb-6"
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
          9:00 AM - 6:00 PM
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
          v-model="form.name"
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
          v-model="form.phone"
          type="text"
          placeholder="Phone Number"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          required
        />
      </div>

      <!-- Service -->
      <div>
        <select
          
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
         
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

      <!-- Message v-model="form.service"   v-model="form.message"-->
      <div>
        <textarea
         
          rows="5"
          placeholder="Write Your Message"
          class="w-full border border-gray-300 rounded-2xl px-5 py-4 outline-none focus:border-[#0B1560]"
          
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
<section class="px-4  sm:px-6 lg:px-10 pb-6">

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
  name: "",
  email: "",
  phone: "",
  // service: "",
  // message: "",
});

const submitForm = async () => {
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
          phone: form.phone,
          email: form.email,
          // mobile_no: form.phone,
          // service: form.service,
          // message: form.message,
        }),
      }
    );

    const data = await response.json();

    if (data.message === "Lead added successfully") {

     
     successMessage.value = true;

setTimeout(() => {
  successMessage.value = false;
}, 4000);
      

      form.name = "";
      form.phone = "";
      form.email = "";
      
      // form.service = "";
      // form.message = "";
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