import time
from pycoingecko import CoinGeckoAPI

def handshake():
  cg = CoinGeckoAPI()
  hnsPrice = cg.get_price(ids='handshake', vs_currencies='usd,btc')
  hnsPriceUsd = hnsPrice['handshake']
  hnsPriceBtc = f"{hnsPriceUsd['btc']:.9f}"
  
  print("Handshake is a decentralized, permissionless naming protocol where every peer is validating and in charge of managing the root DNS naming zone with the goal of creating an alternative to existing Certificate Authorities and naming systems. Names on the internet (top level domains, social networking handles, etc.) ultimately rely upon centralized actors with full control over a system which are relied upon to be honest, as they are vulnerable to hacking, censorship, and corruption. Handshake aims to experiment with new ways the internet can be more secure, resilient, and socially useful with a peer-to-peer system validated by the network's participants.")
  print("Current price: " + str(hnsPriceUsd['usd']) + " USD; " + str(hnsPriceBtc) + " BTC.")

def hnsTools():
  print("HN$ TOOLS is a suite of command line tools to assist users in using Namebase and getting information about HNS.")
  print("HN$ TOOLS was created by rundavidmc/, and it is free to use. All I ask is that you don't distribute it and claim it as yours.")
  print("Note that Namebase ratelimiting still applies. Namebase reserves the right to terminate your account at any time without your knowledge. Please use responsibly.")
  print("My referral link: https://www.namebase.io/register/zczpfp")
  print("My HN$ address: hs1qzts3zt73t8mxyl8jh2ucwypj2g6npzde7q3g0y")

def namebase():
  print("Namebase is an onramp for Handshake. We did not create Handshake, but just like you, we are Directors of Handshake. Our goal is to make Handshake easy-to-use to enable mass adoption, and you can use our platform to easily buy and sell HNS as well as bid on, purchase, sell, and use Handshake names.")
  print("Visit Namebase at http://namebase.io/")
  print("If you don't already have an account, it would be greatly appriciated if you used my referral link: https://www.namebase.io/register/zczpfp. Using this also grants you +10% on all HNS purchases.")

