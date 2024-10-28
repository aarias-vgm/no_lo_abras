import no_lo_abras

if __name__ == "__main__":
    try:
        print("NO LO ABRAS")
        no_lo_abras.run()
    except Exception as e:
        print(f"FATAL EXCEPTION: {e}")
