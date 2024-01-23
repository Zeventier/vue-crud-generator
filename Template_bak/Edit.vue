<template>
    <AppLayout title="__Title__">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                __Title__ Edit
            </h2>
        </template>
        <div class="container">
            <a class="btn btn-primary mb-3 mt-3" :href="route('admin.__table__.index')"><font-awesome-icon
                    icon="fa-solid fa-arrow-left" /></a>
            <div class="container">
                <form @submit.prevent="form.put(route('admin.__table__.update', __table__.id))">
                    <div class="form-group mb-3">
                        <label for="__field__" class="form-label">__Field__</label>
                        <input type="text" class="form-control col-md-6" id="__field__" v-model="form.__field__" />
                    </div>
                    <div class="text-red-500" v-if="form.errors.__field__">
                        {{ form.errors.__field__ }}
                    </div>
                    <button type="submit" class="btn btn-outline-primary">Save</button>
                </form>
            </div>
        </div>
    </AppLayout>
</template>

<script>
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";
import { useForm } from '@inertiajs/vue3';

export default defineComponent({
    components: {
        AppLayout,
    },
    props: {
        __table__: {
            type: Object,
        },
    },
    setup(props) {
        const form = useForm({
            __field__: props.__table__.__field__,
        });

        return {
            form,
        };
    },
});
</script>

<style scoped>
/* Add any custom styling here */
</style>
