from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.embeddings.openai_like import OpenAILikeEmbedding


def test_openai_like_embedding_class():
    names_of_base_classes = [b.__name__ for b in OpenAILikeEmbedding.__mro__]
    assert BaseEmbedding.__name__ in names_of_base_classes
