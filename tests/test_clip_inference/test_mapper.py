import pickle
import os
from clip_retrieval.clip_inference.mapper import ClipMapper
import os


def test_mapper():
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    mapper = ClipMapper(
        enable_image=True,
        enable_text=False,
        enable_metadata=False,
        use_mclip=False,
        clip_model="ViT-B/32",
        use_jit=True,
        mclip_model="",
    )
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tensor_files = [i for i in os.listdir(current_dir + "/test_tensors")]
    for tensor_file in tensor_files:
        with open(current_dir + "/test_tensors/{}".format(tensor_file), "rb") as f:
            tensor = pickle.load(f)
            sample = mapper(tensor)
            assert sample["image_embs"].shape[0] == tensor["image_tensor"].shape[0]
        pass
