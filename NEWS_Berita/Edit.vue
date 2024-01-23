<template>
  <AppLayout title="Berita">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">
        Berita Edit
      </h2>
    </template>
    <div class="container">
      <a class="btn btn-primary mb-3 mt-3" :href="route('admin.berita.index')"
        ><font-awesome-icon icon="fa-solid fa-arrow-left"
      /></a>
      <div class="container">
        <form
          @submit.prevent="form.put(route('admin.berita.update', berita.id))">
          <div class="form-group mb-3">
            <label for="judul" class="form-label">Judul</label>
            <input
              type="text"
              class="form-control col-md-6"
              id="judul"
              v-model="form.judul" />
          </div>
          <div class="text-red-500" v-if="form.errors.judul">
            {{ form.errors.judul }}
          </div>

          <div class="form-group mb-3">
            <label for="penulis" class="form-label">Penulis</label>
            <input
              type="text"
              class="form-control col-md-6"
              id="penulis"
              v-model="form.penulis" />
          </div>
          <div class="text-red-500" v-if="form.errors.penulis">
            {{ form.errors.penulis }}
          </div>

          <div class="form-group mb-3">
            <label for="isi" class="form-label">Isi</label>
            <input
              type="text"
              class="form-control col-md-6"
              id="isi"
              v-model="form.isi" />
          </div>
          <div class="text-red-500" v-if="form.errors.isi">
            {{ form.errors.isi }}
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
import { useForm } from "@inertiajs/vue3";

export default defineComponent({
  components: {
    AppLayout,
  },
  props: {
    berita: {
      type: Object,
    },
  },
  setup(props) {
    const form = useForm({
      __field__: props.berita.__field__,
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
