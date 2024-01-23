<template>
  <AppLayout title="Berita">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">Berita</h2>
    </template>

    <div class="py-12">
      <div class="container">
        <div class="card">
          <div class="card-body">
            <div class="mb-3">
              <a class="btn btn-primary" :href="route('admin.berita.add')"
                ><font-awesome-icon icon="fa-solid fa-square-plus" /> &nbsp;
                Buat baru</a
              >
            </div>
            <table class="table">
              <thead>
                <tr>
                  <th>Judul</th>

                  <th>Penulis</th>

                  <th>Isi</th>

                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in berita" :key="item.id">
                  <td>{{ item.judul }}</td>

                  <td>{{ item.penulis }}</td>

                  <td>{{ item.isi }}</td>

                  <td>
                    <jet-primary-button
                      ><a :href="route('admin.berita.details', item)"
                        ><font-awesome-icon
                          icon="fa-solid fa-magnifying-glass" /></a
                    ></jet-primary-button>
                    &nbsp;
                    <jet-secondary-button
                      ><a :href="route('admin.berita.edit', item)"
                        ><font-awesome-icon
                          icon="fa-solid fa-pen-to-square" /></a
                    ></jet-secondary-button>
                    &nbsp;
                    <jet-danger-button @click="delete_item(item)">
                      <a><font-awesome-icon icon="fa-solid fa-trash-can" /></a>
                    </jet-danger-button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script>
import { useForm } from "@inertiajs/vue3";
import AppLayout from "@/Layouts/AppLayout.vue";
import JetDangerButton from "@/Components/DangerButton.vue";
import JetPrimaryButton from "@/Components/PrimaryButton.vue";
import JetSecondaryButton from "@/Components/SecondaryButton.vue";

export default {
  components: {
    AppLayout,
    JetDangerButton,
    JetPrimaryButton,
    JetSecondaryButton,
  },

  props: {
    berita: {
      type: Array,
    },
  },

  setup() {
    const form = useForm({});

    const delete_item = (berita) => {
      if (confirm("Are you sure you want to delete this berita?")) {
        form.delete(route("admin.berita.delete", berita.id));
      }
    };

    return {
      form,
      delete_item,
    };
  },
};
</script>

<style></style>
