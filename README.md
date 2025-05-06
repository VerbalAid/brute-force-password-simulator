## Key Steps & Logic

1. **Random Index Selection**  
   - `randint(0, N-1)` picks a random position in the character pool, where `N = len(password_chars)`.  

2. **Length‑Matched Trials**  
   - The inner `for` loop runs exactly `len(user_password)` times, ensuring each guess string matches the target password’s length.  

3. **String Accumulation**  
   - In each iteration of the loop, `crack += password_chars[idx]` appends one randomly chosen character to build the trial string.  

4. **Termination Condition**  
   - The `while crack != user_password:` loop continues generating new guesses until the trial string exactly equals the user’s password.  

5. **Metrics & Feedback**  
   - `attempts` is incremented after each full‐length guess to track total trials.  
   - `print("Trying:", crack)` provides real‑time visibility into each guess.  
   - Final `print` statements report the successful match and total number of attempts.  
