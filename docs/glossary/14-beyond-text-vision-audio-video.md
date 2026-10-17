# 14. Beyond text: vision, audio, video

*Cross-cutting: terms from image, speech and video AI that appear in general AI videos*

The same building blocks (Transformers, embeddings, diffusion) applied to pixels and sound. Most of these live in the Generative AI box of Map 1, outside the LLM pipeline.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### CLIP { #clip }

*Also known as:* Contrastive Language-Image Pre-training

A pair of encoders (image and text) trained so matching image–caption pairs get similar embeddings.

**Why it matters:** Lets you search images with words and is the glue inside most image generators and vision-language models.

### Vision-Language Model (VLM) { #vision-language-model }

An LLM with a vision encoder attached, so it can take images as input (GPT-4o, Claude, Gemini, Qwen-VL, LLaVA).

**Why it matters:** Why you can paste a screenshot or a chart into a chat and ask about it.

<small>*Index aliases:* VLM</small>

### Vision encoder / image tokens { #vision-encoder-image-tokens }

Images are cut into patches, encoded (usually by a ViT) and projected into the LLM's token space; a typical image becomes a few hundred to a few thousand tokens.

**Why it matters:** Images are billed and context-limited as tokens, just like text.

<small>*Index aliases:* Image tokens</small>

### Latent diffusion { #latent-diffusion }

*Also known as:* Stable Diffusion

Diffusion run in the compressed latent space of a VAE instead of on raw pixels.

**Why it matters:** Makes image generation many times cheaper, which is what put it on consumer GPUs.

### U-Net / Diffusion Transformer (DiT) { #u-net-diffusion-transformer }

The denoising network inside a diffusion model: a U-Net in older models, a Transformer (DiT) in newer ones (Stable Diffusion 3, Flux, Sora).

**Why it matters:** Another case of "Transformers ate the architecture"; same scaling story as LLMs.

<small>*Index aliases:* DiT, U-Net</small>

### Text encoder / guidance scale (CFG) { #text-encoder-guidance-scale }

The text model that turns the prompt into conditioning vectors, and the knob (classifier-free guidance) controlling how strictly the image follows the prompt.

**Why it matters:** Guidance scale is the image-generation equivalent of temperature: higher is more literal, lower is more creative.

<small>*Index aliases:* CFG, Guidance scale</small>

### ControlNet / image conditioning { #controlnet-image-conditioning }

Add-ons that steer image generation with a sketch, pose, depth map or edge map in addition to text.

**Why it matters:** Gives precise control over composition instead of hoping the prompt lands.

<small>*Index aliases:* ControlNet</small>

### Image LoRA / style fine-tunes { #image-lora-style-fine-tunes }

LoRA adapters trained on a few dozen images to teach a diffusion model a style, product or face.

**Why it matters:** The same LoRA idea from section 9, applied to images; the basis of the custom-model marketplaces.

### Inpainting, outpainting, img2img { #inpainting-outpainting-img2img }

Regenerating part of an image, extending beyond its borders, or transforming an existing image guided by a prompt.

**Why it matters:** The editing operations behind "generative fill" features.

<small>*Index aliases:* Inpainting, img2img</small>

### Automatic Speech Recognition { #automatic-speech-recognition }

*Also known as:* ASR, Whisper

Speech to text. Whisper is the widely used open model.

**Why it matters:** The first step of every voice assistant and the way meeting transcripts are made.

### Text-to-Speech / voice cloning (TTS) { #text-to-speech-voice-cloning }

Generating natural speech from text; cloning reproduces a specific voice from a short sample.

**Why it matters:** The output side of voice assistants, audiobooks and dubbing; cloning is also why voice-based fraud is rising.

<small>*Index aliases:* TTS, Voice cloning</small>

### Speech-to-speech / realtime models { #speech-to-speech-realtime-models }

Models that take audio in and produce audio out directly, with low latency, instead of chaining ASR → LLM → TTS.

**Why it matters:** Makes natural, interruptible voice conversation possible.

<small>*Index aliases:* Realtime voice models</small>

### Omni models { #omni-models }

Single models trained on text, images, audio and video as input, producing text and speech (and sometimes images) as output.

**Why it matters:** Where the frontier is heading: one model for every modality instead of a pipeline of specialists.

<small>*Index aliases:* Omni model</small>

### Text-to-video { #text-to-video }

*Also known as:* Veo, Runway, Kling; OpenAI's Sora, discontinued in 2026

Diffusion or transformer models that generate video clips from a prompt or an image.

**Why it matters:** Same ideas as image generation, far more compute; the current showcase of generative AI, and a crowded market.

<small>*Index aliases:* Sora, Veo / Runway</small>

### World models { #world-models }

Models that learn to predict how an environment evolves (the next frame, the result of an action), used in robotics and games.

**Why it matters:** The argument that video generation is a step toward models that understand physics and planning.

<small>*Index aliases:* World model</small>

### OCR / document AI { #ocr-document-ai }

Extracting text and structure from scanned documents and PDFs; increasingly done by VLMs directly.

**Why it matters:** How invoices, forms and old archives get into RAG pipelines.

<small>*Index aliases:* Document AI</small>

### Multimodal embeddings { #multimodal-embeddings }

Embedding models that map images, text and audio into one shared vector space.

**Why it matters:** Search a photo library with a sentence, or a product catalogue with a picture.

### Deepfake / synthetic media detection { #deepfake-synthetic-media-detection }

Generated images, voices and videos impersonating real people, and the tools that try to detect or watermark them.

**Why it matters:** The main misuse of generative media; provenance standards (C2PA) and watermarks are the response.

<small>*Index aliases:* Deepfake, C2PA / watermarking</small>
