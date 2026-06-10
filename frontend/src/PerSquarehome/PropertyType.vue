<template>
    <section class="pb-4 pt-0 px-4 md:px-10">
        <!-- Heading -->
        <div class="text-center mb-6">
            <h2 class="text-3xl md:text-5xl font-semibold">
                Explore Our
                <span class="text-orange-500 italic">Property Types</span>
            </h2>

            <p class="text-gray-500 mt-4">
                Find Apartments, Villas, Plots and Townships
            </p>
        </div>

        <!-- Property Type Cards -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-7xl mx-auto">
            <div v-for="item in propertyTypes" :key="item.property_type" @click="goToProjects(item.property_type)"
                class="cursor-pointer group">
                <div class="overflow-hidden rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-300">
                    <img :src="item.property_image" :alt="item.property_type"
                        class="w-full h-48 md:h-60 object-cover group-hover:scale-105 transition duration-300" />
                </div>

                <h3 class="text-center mt-4 text-lg md:text-2xl font-semibold">
                    {{ item.property_type }}
                </h3>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const propertyTypes = ref([]);

const getPropertyTypes = async () => {
    try {
        const response = await fetch(
            "/api/method/per_sqr_ft.api.property.get_property_types"
        );

        const data = await response.json();

        propertyTypes.value = data.message || [];
    } catch (error) {
        console.error("Error fetching property types:", error);
    }
};

const goToProjects = (propertyType) => {
    router.push(`/property/${propertyType}`);
};

onMounted(() => {
    getPropertyTypes();
});
</script>