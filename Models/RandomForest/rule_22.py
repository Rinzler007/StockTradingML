def findDecision(obj):
   # Feature: RSI, Instances: 115, Entropy: 0.9986
   if obj[1] == 'Hold':
      # Feature: BB, Instances: 93, Entropy: 0.9999
      if obj[3] == 'Sell':
         # Feature: Closing, Instances: 63, Entropy: 0.9852
         if obj[0]>4.942:
            # Feature: MACD, Instances: 61, Entropy: 0.9764
            if obj[2] == 'Sell':
               # Feature: SMA2, Instances: 36, Entropy: 0.9911
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 19, Entropy: 0.998
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 17, Entropy: 0.9774
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               # Feature: SMA1, Instances: 25, Entropy: 0.9427
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 18, Entropy: 0.9183
                  if obj[5] == 'Sell':
                     return 'No'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.9852
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]<=4.942:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[3] == 'Hold':
         # Feature: SMA1, Instances: 26, Entropy: 0.8905
         if obj[4] == 'Buy':
            # Feature: MACD, Instances: 17, Entropy: 0.7871
            if obj[2] == 'Buy':
               # Feature: Closing, Instances: 13, Entropy: 0.7793
               if obj[0]>4.942:
                  # Feature: SMA2, Instances: 13, Entropy: 0.7793
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2] == 'Sell':
               # Feature: Closing, Instances: 4, Entropy: 0.8113
               if obj[0]>4.942:
                  # Feature: SMA2, Instances: 4, Entropy: 0.8113
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 9, Entropy: 0.9911
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 5, Entropy: 0.971
               if obj[0]>4.942:
                  # Feature: MACD, Instances: 5, Entropy: 0.971
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: Closing, Instances: 4, Entropy: 0.8113
               if obj[0]>4.942:
                  # Feature: MACD, Instances: 4, Entropy: 0.8113
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[3] == 'Buy':
         # Feature: Closing, Instances: 4, Entropy: 0.8113
         if obj[0]>4.942:
            return 'No'
         elif obj[0]<=4.942:
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'No'
   elif obj[1] == 'Sell':
      # Feature: SMA1, Instances: 15, Entropy: 0.3534
      if obj[4] == 'Buy':
         # Feature: MACD, Instances: 11, Entropy: 0.4395
         if obj[2] == 'Buy':
            # Feature: SMA2, Instances: 10, Entropy: 0.469
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 9, Entropy: 0.5033
               if obj[0]>4.942:
                  # Feature: BB, Instances: 9, Entropy: 0.5033
                  if obj[3] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         elif obj[2] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[4] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[1] == 'Buy':
      return 'No'
   else:
      return 'No'
