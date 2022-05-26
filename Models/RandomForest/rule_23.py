def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9758
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 69, Entropy: 0.9816
      if obj[0]<=791.3599849999998:
         # Feature: RSI, Instances: 63, Entropy: 0.9955
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 61, Entropy: 0.9951
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 31, Entropy: 0.9383
               if obj[4] == 'Sell':
                  # Feature: MACD, Instances: 23, Entropy: 0.9656
                  if obj[2] == 'Buy':
                     return 'No'
                  elif obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Buy':
                  # Feature: MACD, Instances: 8, Entropy: 0.8113
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 30, Entropy: 0.9871
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 22, Entropy: 0.994
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 8, Entropy: 0.5436
                  if obj[2] == 'Sell':
                     return 'Yes'
                  elif obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[1] == 'Buy':
            return 'No'
         elif obj[1] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[0]>791.3599849999998:
         return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 40, Entropy: 0.3843
      if obj[1] == 'Hold':
         # Feature: SMA2, Instances: 22, Entropy: 0.5746
         if obj[5] == 'Buy':
            # Feature: SMA1, Instances: 18, Entropy: 0.65
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 13, Entropy: 0.3912
               if obj[2] == 'Buy':
                  # Feature: Closing, Instances: 11, Entropy: 0.4395
                  if obj[0]<=791.3599849999998:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: Closing, Instances: 5, Entropy: 0.971
               if obj[0]<=791.3599849999998:
                  # Feature: MACD, Instances: 5, Entropy: 0.971
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[5] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: RSI, Instances: 6, Entropy: 0.9183
      if obj[1] == 'Hold':
         # Feature: Closing, Instances: 4, Entropy: 1.0
         if obj[0]<=791.3599849999998:
            # Feature: MACD, Instances: 4, Entropy: 1.0
            if obj[2] == 'Sell':
               # Feature: SMA1, Instances: 4, Entropy: 1.0
               if obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 4, Entropy: 1.0
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[1] == 'Buy':
         return 'No'
      else:
         return 'No'
   else:
      return 'No'
