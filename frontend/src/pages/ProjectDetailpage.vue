<template>
    <section class="max-w-7xl mx-auto md:px-16 pt-1">
        <div class="relative overflow-hidden ">

            <!-- Project Image -->
            <img :src="project.thumbnail_image" :alt="project.project_name"
                class="w-full mx-auto h-[280px] md:h-[530px] object-cover" />

            <!-- Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

            <!-- Content -->
            <div class="absolute bottom-0 left-0 w-full p-6 md:p-10">
                <h1 class="text-white text-lg md:text-5xl font-bold mb-2 md:mb-4">
                    {{ project.project_name }}
                </h1>

                <h2 class="text-gray-200 text-xs md:text-3xl font-medium md:font-bold mb-3 md:mb-5">
                    {{ project.full_location }}
                </h2>

                <!-- Navigation Links -->
                <div class="hidden  md:flex flex-wrap gap-x-4 gap-y-2 text-white text-base md:text-lg">

                    <a href="#overview" class="hover:text-orange-400 text-[16px] md:text-[18px]">Overview</a>
                    <span>|</span>

                    <a href="#price" class="hover:text-orange-400 text-[16px] md:text-[18px]">Price</a>
                    <span>|</span>

                    <a href="#floor-plan" class="hover:text-orange-400 text-[16px] md:text-[18px]">Floor Plan</a>
                    <span>|</span>

                    <a href="#photos" class="hover:text-orange-400 text-[16px] md:text-[18px]">Photos</a>
                    <span>|</span>

                    <a href="#master-plan" class="hover:text-orange-400 text-[16px] md:text-[18px]">Master Plan</a>
                    <span class="text-[16px] md:text-[22px]">|</span>

                    <a href="#amenities" class="hover:text-orange-400 text-[16px] md:text-[18px]">Amenities</a>
                    <span>|</span>

                    <a href="#location" class="hover:text-orange-400 text-[16px] md:text-[18px]">Location</a>

                </div>

            </div>

        </div>
    </section>

    <section class=" max-w-7xl mx-auto px-4 pt-12 ">

        <!-- <div class="grid grid-cols-12 gap-8"> -->
        <div class="grid grid-cols-1 md:grid-cols-12 gap-8">

            <!-- Left Side -->
            <div class="col-span-8">

                <!-- Overview -->
                <div class="bg-white px-8">

                    <div class="mb-8 ">

                        <h2 class="text-4xl font-bold text-gray-900">
                            {{ project.description_heading || 'Overview' }}
                        </h2>

                        <div class="w-24 h-1 bg-orange-500 rounded-full mt-4"></div>

                    </div>

                    <div class="prose prose-lg max-w-none text-gray-700 leading-relaxed" v-html="project.description">
                    </div>

                </div>

                <!-- Youtube Video -->
                <div class="mt-2 mx-2 md:mx-10" v-if="project.youtube_link?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Project Walkthrough
                    </h2>
                    <div class="w-24 h-1 bg-orange-500 rounded-full mt-4 mb-8"></div>



                    <div class="overflow-hidden rounded-3xl shadow-xl">

                        <iframe class="w-full  h-[220px] md:h-[420px]" :src="project.youtube_link" title="Project Video"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen>
                        </iframe>

                    </div>

                </div>

                <!--Gallery section-->
                <!-- Gallery Section -->
                <div class="mt-12 md:mx-10" v-if="project.gallery_images?.length">

                    <h2 class="text-3xl   font-bold text-gray-900 mb-4">
                        Project Gallery
                    </h2>

                    <div class="w-24 h-1  bg-orange-500 rounded-full mb-8"></div>

                    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">

                        <div v-for="(gallery_images, index) in project.gallery_images" :key="index"
                            class="w-full overflow-hidden rounded-2xl shadow-lg  ">

                            <img :src="gallery_images.gallery_images" :alt="'Gallery Image ' + index"
                                class="w-full h-[180px] md:h-[200px] object-cover hover:scale-105 transition duration-300" />

                        </div>

                    </div>

                </div>
                <!-- Property Configuration -->
                <div class="mt-12  md:mx-10" v-if="project.property_details?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Property Configuration
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-8"></div>

                    <div v-for="(detail, index) in project.property_details" :key="index"
                        class="overflow-hidden rounded-2xl border border-gray-200 bg-white">

                        <table class="w-full">

                            <tbody>

                                <!-- <tr class="border-b">
                                    <td class="w-4 p-4 text-center  text-4xl">📍</td>
                                    <td class="p-4   border-r border-gray-300">Project Location</td>
                                    <td class="p-4 text-center w-[35%]">
                                        <div class="max-w-[400px] mx-auto leading-7">
                                            {{ project.full_location }}
                                        </div>
                                    </td>
                                </tr> -->

                                <tr class="border-b" v-if="project.full_location">

                                    <!-- <div class="">
                                        <td class="w-[120px] p-4 text-center  border-gray-200 text-[50px]">
                                            📍
                                        </td>
                                    </div> -->
                                    <td class="w-[120px] p-4 text-center">
                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">
                                            📍
                                        </div>
                                    </td>

                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">
                                        Project Location
                                    </td>

                                    <td class="w-[45%] p-4 text-center">
                                        {{ project.full_location }}
                                    </td>

                                </tr>

                                <tr class="border-b" v-if="detail.total_land_area">
                                    <td class="w-[120px] p-4 text-center">

                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">

                                            🌳

                                        </div>

                                    </td>
                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">Total Land
                                        Area</td>
                                    <td class="w-[45%] p-4 text-center">
                                        {{ detail.total_land_area }}
                                    </td>
                                </tr>

                                <tr class="border-b" v-if="detail.no_of_units">
                                    <td class="w-[120px] p-4 text-center">

                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">

                                            🏢

                                        </div>

                                    </td>
                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">No. of
                                        Units</td>
                                    <td class="w-[45%] p-4 text-center text-gray-900">
                                        {{ detail.no_of_units }}
                                    </td>
                                </tr>

                                <tr class="border-b" v-if="detail.towers_and_blocks">
                                    <td class="w-[120px] p-4 text-center">

                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">



                                            🏗️</div>

                                    </td>
                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">Towers &
                                        Blocks</td>
                                    <td class="w-[45%] p-4 text-center">
                                        {{ detail.towers_and_blocks }}
                                    </td>
                                </tr>

                                <tr class="border-b" v-if="detail.unit_variants">
                                    <td class="w-[120px] p-4 text-center">

                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">



                                            🏠</div>

                                    </td>
                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">Unit
                                        Variants</td>
                                    <td class="w-[45%] p-4 text-center">
                                        {{ detail.unit_variants }}
                                    </td>
                                </tr>

                                <tr v-if="detail.possession_time">
                                    <td class="w-[120px] p-4 text-center">

                                        <div
                                            class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-[40px]">



                                            📅</div>

                                    </td>
                                    <td class="w-[35%] p-4 text-center border-r border-gray-200 font-medium">Possession
                                        Time</td>
                                    <td class="w-[45%] p-4 text-center">
                                        {{ detail.possession_time }}
                                    </td>
                                </tr>

                            </tbody>

                        </table>

                    </div>

                </div>

                <!-- Unit Configuration -->
                <div class="mt-12 md:mx-10" v-if="project.property_unit && project.property_unit.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-2">
                        Available Unit Options
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-6"></div>

                    <div
                        class="overflow-hidden border border-gray-200 bg-gradient-to-r from-orange-50 to-amber-100 rounded-xl">

                        <table class="w-full">

                            <thead>
                                <tr class="bg-blue-800 text-white">


                                    <th class="py-2 px-4 text-center border-r border-orange-300">
                                        Unit Type
                                    </th>

                                    <th class="py-2 px-4 text-center">
                                        Size in Sq.Ft
                                    </th>

                                </tr>
                            </thead>

                            <tbody>
                                <tr v-for="(unit, index) in project.property_unit" :key="index"
                                    class="border-b border-orange-200 even:bg-orange-50">
                                    <td class="py-2 px-4 text-center border-r border-orange-200">
                                        {{ unit.unit_type }}
                                    </td>

                                    <td class="py-2 px-4 text-center">
                                        {{ unit.size_in_sqft }}
                                    </td>
                                </tr>
                            </tbody>

                        </table>

                    </div>

                </div>

                <!-- Location Map -->
                <div class="mt-12 md:mx-10" v-if="project.project_location_map_embed?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Location Map
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-8"></div>

                    <div class="overflow-hidden rounded-2xl shadow-lg border">

                        <iframe :src="project.project_location_map_embed" width="100%" height="380" style="border:0;"
                            allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
                        </iframe>

                    </div>

                </div>


                <!-- Master Plan -->
                <div class="mt-12 md:mx-10" v-if="project.master_plan_images?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Master Plan
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-8"></div>

                    <div class="bg-white  rounded-3xl shadow-lg border overflow-hidden">

                        <div class="p-5 border-b">
                            <h3 class="text-xl font-semibold">
                                Project Master Plan
                            </h3>

                            <p class="text-gray-500 mt-1">
                                Explore the complete project layout and development plan.
                            </p>
                        </div>

                        <img :src="project.master_plan_images" alt="Master Plan" class="w-full h-auto object-cover" />

                    </div>

                </div>


                <!-- Specifications -->
                <div class="mt-12 md:mx-10">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Project Specifications
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-8"></div>

                    <div class="overflow-hidden border border-gray-200 bg-white">

                        <table class="w-full">

                            <tbody>

                                <!-- Structure -->
                                <tr class="border-b border-gray-200">

                                    <td class="w-[180px] p-6 text-center border-r border-gray-200">

                                        <div
                                            class="w-20 h-20 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-5xl">
                                            🏢
                                        </div>

                                        <h3 class="font-semibold text-xl mt-4">
                                            Structure
                                        </h3>

                                    </td>

                                    <td class="p-6">

                                        <ul class="list-disc pl-6 space-y-3 text-gray-700">
                                            <li>RCC Framed Structure with Solid Blocks for wall masonry.</li>
                                            <li>External walls are 6" thick & internal walls are 4" thick.</li>
                                        </ul>

                                    </td>

                                </tr>

                                <!-- Flooring -->
                                <tr class="border-b border-gray-200">

                                    <td class="p-6 text-center border-r border-gray-200">

                                        <div
                                            class="w-20 h-20 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-5xl">
                                            🔶
                                        </div>

                                        <h3 class="font-semibold text-xl mt-4">
                                            Flooring
                                        </h3>

                                    </td>

                                    <td class="p-6">

                                        <ul class="list-disc pl-6 space-y-3 text-gray-700">
                                            <li>Laminated AC4 Grade Wooden Flooring for Master Bedroom.</li>
                                            <li>Imported Marble flooring in living room and dining.</li>
                                            <li>Matt-finish tiles for the kitchen.</li>
                                            <li>IS Standard tiles (600×1200) in all bedrooms.</li>
                                            <li>Anti-skid tiles for bathroom and balcony flooring.</li>
                                        </ul>

                                    </td>

                                </tr>

                                <!-- Doors -->
                                <tr class="border-b border-gray-200">

                                    <td class="p-6 text-center border-r border-gray-200">

                                        <div
                                            class="w-20 h-20 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-5xl">
                                            🚪
                                        </div>

                                        <h3 class="font-semibold text-xl mt-4">
                                            Doors
                                        </h3>

                                    </td>

                                    <td class="p-6">

                                        <ul class="list-disc pl-6 space-y-3 text-gray-700">
                                            <li>Main door with teak wood frame.</li>
                                            <li>Premium flush shutters for internal doors.</li>
                                            <li>UPVC sliding doors for balconies.</li>
                                        </ul>

                                    </td>

                                </tr>

                                <!-- Electrical -->
                                <tr>

                                    <td class="p-6 text-center border-r border-gray-200">

                                        <div
                                            class="w-20 h-20 mx-auto flex items-center justify-center rounded-full bg-orange-100 text-5xl">
                                            ⚡
                                        </div>

                                        <h3 class="font-semibold text-xl mt-4">
                                            Electrical
                                        </h3>

                                    </td>

                                    <td class="p-6">

                                        <ul class="list-disc pl-6 space-y-3 text-gray-700">
                                            <li>Concealed copper wiring with modular switches.</li>
                                            <li>100% power backup for common areas.</li>
                                            <li>Provision for AC and TV points in all rooms.</li>
                                        </ul>

                                    </td>

                                </tr>

                            </tbody>

                        </table>

                    </div>

                </div>

                <!-- Animation Component -->
                <!-- Project Highlights -->
                <div class="mt-12 mx-10" v-if="project.property_amenities?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-4">
                        Project Amenities
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-8"></div>

                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">

                        <div v-for="(item, index) in project.property_amenities" :key="index"
                            class="bg-white rounded-xl shadow border p-3 text-center">

                            <img :src="item.amenities_images" :alt="item.amenities_name"
                                class="w-30 h-30 mx-auto object-contain">

                            <h3 class="text-sm font-medium mt-3">
                                {{ item.amenities_name }}
                            </h3>

                        </div>

                    </div>

                </div>

                <!--  Unit Configuration & Pricing -->
                <div class="mt-6 md:mx-10" v-if="project.property_unit?.length">

                    <h2 class="text-3xl font-bold text-gray-900 mb-2">
                        Unit Configuration & Pricing
                    </h2>

                    <div class="w-24 h-1 bg-orange-500 rounded-full mb-6"></div>

                    <div
                        class="overflow-hidden border border-gray-200 bg-gradient-to-r from-orange-50 to-amber-100 rounded-xl">

                        <table class="w-full">

                            <thead>
                                <tr class="bg-blue-800 text-white">


                                    <th class="py-2 px-4 text-center border-r border-orange-300">
                                        Unit Type
                                    </th>

                                    <th class="py-2 px-4 border-r text-center">
                                        Size in Sq.Ft
                                    </th>
                                    <th class="py-2 px-4 text-center">
                                        Approx. Starting Price
                                    </th>

                                </tr>
                            </thead>

                            <tbody>
                                <tr v-for="(unit, index) in project.property_unit" :key="index"
                                    class="border-b border-orange-200 even:bg-orange-50">
                                    <td class="py-2 px-4 text-center border-r border-orange-200">
                                        {{ unit.unit_type }}
                                    </td>

                                    <td class="py-2 px-4 border-r text-center">
                                        {{ unit.size_in_sqft }}
                                    </td>

                                    <td class="py-2 px-4 text-center">
                                        <!-- {{ unit.approx.all_inclusive_price }} -->
                                        {{ unit.approx_all_inclusive_price }}
                                    </td>
                                </tr>

                            </tbody>

                        </table>

                    </div>

                </div>


            </div>


            <!-- Right Side Sticky Form -->
            <div class="hidden md:block col-span-4">

                <div class="sticky top-24">

                    <div class="rounded-3xl shadow-2xl border p-6 bg-white">

                        <div class="text-center mb-6">

                            <h3 class="text-4xl font-bold">
                                Enquire Now
                            </h3>

                            <p class="text-gray-500 mt-2 text-xl">
                                Get Floor Plans & Pricing
                            </p>
                            <div v-if="sucessMessage" class="mb-4 p-3 text-green-700 rounded-lg text-center">
                                Your query has been sent to the contact team.
                            </div>

                            <!-- Error Message -->
                            <div v-if="errorMessage" class="mb-4 p-3 bg-red-100 text-red-700 rounded-lg text-center">
                                Something went wrong. Please try again.
                            </div>


                        </div>

                        <form class="space-y-4" @submit.prevent="submitContactForm">

                            <input type="text" v-model="contctDetails.name" placeholder="Your Name"
                                class="w-full px-4 py-2 border rounded-xl outline-none" />

                            <input type="text" v-model="contctDetails.phone" placeholder="Phone Number"
                                class="w-full px-4 py-2 border rounded-xl outline-none" />

                            <input type="email" v-model="contctDetails.email" placeholder="Email Address"
                                class="w-full px-4 py-2 border rounded-xl outline-none" />

                            <textarea rows="3" placeholder="Your Requirement"
                                class="w-full px-4 py-2 border rounded-xl outline-none">
                        </textarea>

                            <button
                                class="w-full bg-orange-600 hover:bg-orange-700 text-white py-3 rounded-xl font-medium">
                                Submit Enquiry
                            </button>

                        </form>


                    </div>

                </div>

            </div>

        </div>

    </section>



</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import FeatureImages from "../PerSquarehome/FeatureImages.vue";



const route = useRoute();

const project = ref({});
const contctDetails = reactive({
    name: "",
    phone: "",
    email: "",

})

const sucessMessage = ref(false)
const errorMessage = ref(false);

onMounted(async () => {
    try {
        const url = route.params.url;

        const response = await fetch(
            `/api/method/per_sqr_ft.api.property.get_project_details?url=${url}`
        );

        const data = await response.json();

        project.value = data.message;

        console.log(project.value);
        console.log(project.gallery_images[0])

    } catch (error) {
        console.error("Error loading project:", error);
    }
});


const submitContactForm = async () => {
    try {



        const response = await axios.post(
            "/api/method/per_sqr_ft.api.lead.add_lead",
            {
                name: contctDetails.name,
                phone: contctDetails.phone,
                email: contctDetails.email,
            },
            {
                headers: {
                    "Content-Type": "application/json",
                },
            }
        );
        console.log(response.data);
        // if (response.data.message === "Lead added successfully") {
        //     alert("sent your data")
        // }
        // else {
        //     alert('something went wrong')
        // }

        sucessMessage.value = true

        setTimeout(() => {
            sucessMessage.value = false
        }, 4000)

        contctDetails.name = "",
            contctDetails.phone = "",
            contctDetails.email = ""

    }
    catch (error) {


        errorMessage.value = true;

        setTimeout(() => {
            errorMessage.value = false;
        }, 4000);
        console.log(error);


    }

}
</script>