from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    context = {"title": "News"}
    return render(request, "blog/index.html", context)


def post(request):
    return redirect("blog-home")


def post_details(request, slug):
    dummy_data = """
        <div>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium corporis facere harum id in iusto minus
        modi molestiae odio omnis pariatur possimus rem repellendus reprehenderit, similique sunt velit vitae
        voluptatem.
    </div>
    <div>Commodi enim harum reiciendis sequi sint ut? A assumenda atque debitis dignissimos et fugiat ipsa ipsam
        mollitia nam nemo, omnis possimus quis quos, sed sequi. Adipisci amet consequatur excepturi exercitationem!
    </div>
    <div>Aut autem commodi eos fuga mollitia voluptate! Autem cum eaque eligendi labore molestias nihil quia quidem,
        repudiandae ut veniam! Amet consequuntur corporis itaque iusto libero placeat, praesentium unde vero voluptatem!
    </div>
    <div>Ab cupiditate debitis doloremque expedita fugit incidunt magni praesentium quam quisquam, recusandae repellat
        sequi tempora voluptatem. Amet animi earum eligendi excepturi iusto, laboriosam, libero molestias officiis
        quaerat ratione tempora voluptas?
    </div>
    <div>Labore minima neque nostrum officiis placeat ratione rem! Aspernatur cumque eos explicabo placeat possimus. Ab
        cum deleniti distinctio ipsum nemo pariatur quam quibusdam reiciendis reprehenderit voluptatum? Est nihil quae
        sapiente.
    </div>
    <div>Ad cum dicta enim mollitia neque perspiciatis recusandae voluptate! Doloremque, earum eligendi error harum
        incidunt iure laboriosam mollitia nesciunt non officiis perferendis qui quibusdam quo rerum sed tempore tenetur
        ullam!
    </div>
    <div>A debitis delectus deserunt dolorem eligendi fuga harum incidunt iusto labore non nostrum, numquam officiis,
        perspiciatis quo ratione recusandae, repellendus reprehenderit vitae? Aut commodi dicta ex fuga perspiciatis,
        sit voluptas.
    </div>
    <div>Accusamus cum dignissimos doloremque fuga mollitia nemo, nulla soluta? Alias amet consectetur distinctio enim
        eos excepturi fugiat illo incidunt inventore iste iure natus, obcaecati pariatur, quos, saepe sapiente soluta
        velit?
    </div>
    """
    context = {
        "title": f"News Post {slug}",
        "data": dummy_data,
        "image": f"img{slug}.jpeg",
    }
    return render(request, "blog/post-detail.html", context)
