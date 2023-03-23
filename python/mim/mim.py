#! /usr/bin/env python3
from audio import audio_open_write
from auth import authorization_metadata
from common import (
    make_channel,
    build_synthesis_request,
)
from tinkoff.cloud.tts.v1 import tts_pb2_grpc, tts_pb2

API_KEY=""
SECRET_KEY=""
def main():
    with audio_open_write('output_6.wav', 1, 48000) as audio_writer:
        stub = tts_pb2_grpc.TextToSpeechStub(make_channel(args))
        request = {
            "input": {
                "text": "\320\237\321\200\320\270\320\262\320\265\321\202! \320\257 \320\220\320\273\321\221\320\275\320\260. \320\257 \320\277\320\276\320\274\320\276\320\263\321\203 \320\262 \320\276\320\267\320\262\321\203\321\207\320\272\320\265 \320\272\320\275\320\270\320\263, \320\275\320\276\320\262\320\276\321\201\321\202\320\265\320\271, \320\276\320\261\321\200\320\260\320\267\320\276\320\262\320\260\321\202\320\265\320\273\321\214\320\275\321\213\321\205 \320\272\321\203\321\200\321\201\320\276\320\262, \320\260 \321\202\320\260\320\272\320\266\320\265 \320\274\320\276\320\263\321\203 \320\261\321\213\321\202\321\214 \321\202\320\262\320\276\320\270\320\274 \320\275\320\260\320\277\320\260\321\200\320\275\320\270\320\272\320\276\320\274 \320\264\320\273\321\217 \320\274\320\265\320\264\320\270\321\202\320\260\321\206\320\270\320\270."
            },
            "voice": {
                "name": "alyona"  
            },
            "audio_config": {
                "audio_encoding": tts_pb2.LINEAR16,
                "sample_rate_hertz": 48000
            },
        }
        print(request)
        metadata = authorization_metadata(API_KEY, SECRET_KEY, "tinkoff.cloud.tts")
        responses = stub.StreamingSynthesize(request, metadata=metadata)
        for stream_response in responses:
            audio_writer.write(stream_response.audio_chunk)


if __name__ == "__main__":
    main()
