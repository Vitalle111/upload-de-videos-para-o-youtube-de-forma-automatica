import os
import datetime
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz  # Biblioteca para manipulação de fusos horários

# Configurações
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRET_FILE = "client_secrets.json"
TOKEN_FILE = "token.pickle"
VIDEO_FOLDER = "D:/GRAVAÇOES DO OBS/VIDEOS RENDERIZADOS/SHOTS/SHOTS 1"
POST_TIMES = [12, 16, 18]  # Horários de postagem no horário de Brasília (GMT-3)

# ID da playlist de "Valorant" (substitua pelo ID real da playlist)
PLAYLIST_ID = "PLEh1w_8eg3xML6cqaG4b4f6DeEEtHW5pf"

# Fuso horário de Brasília
BRAZIL_TZ = pytz.timezone("America/Sao_Paulo")

def authenticate_youtube():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)
    
    return build("youtube", "v3", credentials=creds)

def upload_video(youtube, file_path, title, description, tags, category_id, publish_time):
    if not os.path.exists(file_path):
        print(f"❌ Erro: Arquivo não encontrado - {file_path}")
        return
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category_id,
                "defaultLanguage": "pt",
                "defaultAudioLanguage": "pt",
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": publish_time.isoformat(),  # Formato correto UTC
                "madeForKids": False  
            }
        },
        media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"✅ Vídeo agendado para {publish_time.astimezone(BRAZIL_TZ).strftime('%d/%m/%Y %H:%M')} BRT: https://youtu.be/{response['id']}")

def schedule_videos(video_list):
    youtube = authenticate_youtube()
    today = datetime.datetime.now(BRAZIL_TZ)  # Obtém a data e hora no horário de Brasília
    
    for index, video in enumerate(video_list):
        day_offset = index // len(POST_TIMES)  
        time_index = index % len(POST_TIMES)  
        
        # Define o horário correto no fuso de Brasília
        publish_time_brt = today + datetime.timedelta(days=day_offset)
        publish_time_brt = publish_time_brt.replace(hour=POST_TIMES[time_index], minute=0, second=0, microsecond=0)
        
        # Converte para UTC antes de enviar para o YouTube
        publish_time_utc = publish_time_brt.astimezone(pytz.utc)
        
        upload_video(youtube, os.path.join(VIDEO_FOLDER, video["file_name"]), video["title"], video["description"], video["tags"], video["category_id"], publish_time_utc)

# Lista de vídeos para envio automático
videos = [
    {"file_name": "video4.mp4", "title": "OLHA A MINHA JOGADA #valorantgaming #valorantfunny #valorantclip #valorantmemes #valorantedit #rush", "description": "#Valorant #ValorantGameplay #ValorantHighlights #ValorantMontage #ValorantGuide #ValorantTips #ValorantTricks #ValorantBestPlays #ValorantClips #ValorantMoments #ValorantBrasil #ValorantRanked #ValorantUpdate #ValorantPatchNotes #ValorantEsports #ValorantPro #ValorantCompetitive #ValorantStreamer #ValorantDicas #ValorantNews #ValorantGameplayBR #ValorantSettings #ValorantStrategy #ValorantAgents #ValorantWeapons #ValorantAimbot #ValorantCrosshair #ValorantTactics #ValorantSetup #ValorantTournament #ValorantTipsAndTricks #ValorantFun #ValorantHeadshot #ValorantSkills #ValorantFunnyMoments #ValorantFragMovie #ValorantNoob #ValorantGameplayHighlights #ValorantChampions #ValorantProPlayer #ValorantKilljoy #ValorantJett #ValorantReyna #ValorantRaze #ValorantSage #ValorantViper #ValorantYoru #ValorantRankedGameplay #ValorantAct #ValorantEpisode #ValorantMeta #ValorantCustomGames #ValorantSoloQueue #ValorantFunny #ValorantMomentsBR #ace #rush #meme #rush", "tags": ["Valorant", "ValorantGameplay", "ValorantHighlights", "ValorantMontage", "ValorantGuide", "ValorantTips", "ValorantTricks", "ValorantBestPlays", "ValorantClips", "ValorantMoments", "ace", "rush", "meme"], "category_id": "20", "game_title": "Valorant"},

{"file_name": "video5.mp4", "title": "OLHA O QUE EU FIZ NO #valorant #valorantclips #valorantgaming #valorantfunny #valorantclip #valorant", "description": "#Valorant, #ValorantGameplay, #ValorantMontage, #ValorantTips, #ValorantGuide, #ValorantHighlights, #ValorantRanked, #ValorantClutch, #ValorantFunnyMoments, #ValorantBestPlays, #ValorantProPlay, #ValorantStrategy, #ValorantTutorial, #ValorantEpicMoments, #ValorantStreamer, #ValorantLive, #ValorantEsports, #ValorantUpdate, #ValorantPatchNotes, #ValorantNewAgent, #ValorantCompetitive, #ValorantViral, #ValorantGuide, #ValorantTricks, #ValorantEpicPlays, #ValorantTeamplay, #ValorantBestMoments, #ValorantTactics, #ValorantMeta, #ValorantBeginner, #ValorantAdvanced, #ValorantFrag, #ValorantAce, #ValorantHeadshot, #ValorantOutplays, #ValorantWin, #ValorantComeback, #ValorantSkill, #ValorantReaction, #ValorantChallenge, #ValorantEvents, #ValorantSeason, #ValorantPatch, #ValorantGameplay2024, #ValorantTipsAndTricks, #ValorantBestOf, #ValorantOutplay, #ValorantMoments, #ValorantContent, #ValorantFunnymoments #ace #rush #meme #rush #valorantbrasil #valorantlive", "tags": ["Valorant", "ValorantGameplay", "ValorantHighlights", "ValorantMontage", "ValorantGuide", "ValorantTips", "ValorantTricks", "ValorantBestPlays", "ValorantClips", "ValorantMoments", "ace", "rush", "meme"], "category_id": "20", "game_title": "Valorant"},

]

# Agendar os vídeos corretamente
schedule_videos(videos)
