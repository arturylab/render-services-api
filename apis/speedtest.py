from fastapi import APIRouter
import speedtest

router = APIRouter()

@router.get("/")
def get_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    return {
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2),
        "ping": ping,
        "server_name": st.best['name'],
        "server_host": st.best['host']
    }
